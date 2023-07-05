import glob
import librosa
import torch
import pandas as pd
import os

from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from sklearn.preprocessing import LabelEncoder

from pytorch_lightning import LightningDataModule


class AudioDataset(Dataset):
    def __init__(self, root_dir, data_frame, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.data_frame = data_frame


    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, idx):
        audio_path = self.data_frame.iloc[idx]["filename"]
        label = self.data_frame.iloc[idx]["category"]

        # Load audio data and perform any desired transformations
        sig, sr = librosa.load(audio_path, sr=44100, mono=True)
        sig = librosa.util.fix_length(sig, size=10*sr) 
        sig_t = torch.tensor(sig)
        padding_mask = torch.zeros(1, sig_t.shape[0]).bool().squeeze(0)
        if self.transform:
            sig_t = self.transform(sig_t)


        return sig_t, padding_mask, label


class ECS50DataModule(LightningDataModule):
    def __init__(
        self,
        root_dir: str = "/content/drive/MyDrive/빅프/응급상황/Validation/",
        batch_size: int = 8,
        split_ratio=0.8,
        transform=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.root_dir = root_dir
        self.batch_size = batch_size
        self.split_ratio = split_ratio
        self.transform = transform

        self.setup()

    def prepare_data(self):
        pass

    def setup(self, stage=None):
      class_to_num = {"[원천]1.강제추행(성범죄)_1":0, "[원천]2.강도범죄_1":1, "[원천]3.절도범죄_1":2, "[원천]4.폭력범죄_1":3, "[원천]5.화재_1":4, "[원천]6.갇힘_1":5 , "[원천]7.응급의료_1":6, "[원천]8.전기사고_1":7, "[원천]9.가스사고_1":8, 
                "[원천]10.낙상_1":9, "[원천]11.붕괴사고_1":10, "[원천]14.도움요청_1":11, "[원천]15.실내_1":12, "[원천]15.실내_2":12, "[원천]15.실내_3":12, "[원천]15.실내_4":12, "[원천]15.실내_5":12, "[원천]16.실외_1":13, "[원천]16.실외_2":13, "[원천]16.실외_3":13 }
      data_frame = pd.DataFrame(columns=['filename', 'category'])
      for classes in os.listdir(self.root_dir):
          class_num = class_to_num[classes]
          file_name = os.listdir(os.path.join(self.root_dir, classes))
          file_path = []
          for files in file_name:
            file_path.append(os.path.join(self.root_dir, classes, files))
          data_frame_temp = pd.DataFrame({'filename': file_path, 'category':[class_num for _ in range(len(os.listdir(os.path.join(self.root_dir, classes))))]})
          data_frame = data_frame.append(data_frame_temp, ignore_index = True)
      
      data_frame = data_frame.sample(frac=1).reset_index(
          drop=True
      )  # shuffle the data frame
      split_index = int(len(data_frame) * self.split_ratio)
      self.train_set = data_frame.iloc[:split_index, :]
      self.val_set = data_frame.iloc[split_index:, :]

    def train_dataloader(self):
        train_df = AudioDataset(
            root_dir=self.root_dir, data_frame=self.train_set, transform=self.transform
        )

        return DataLoader(train_df, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        val_df = AudioDataset(
            root_dir=self.root_dir, data_frame=self.val_set, transform=self.transform
        )

        return DataLoader(val_df, batch_size=self.batch_size, shuffle=False)
