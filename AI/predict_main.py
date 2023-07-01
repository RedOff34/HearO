import torch 
from AI.BEATs_eval import predict
from AI import transferLearning
import os
#import sms

data_path = './AI/sound/'
checkpoint_path = './AI/model/BEATs_iter3+_AS2M_10s.ckpt'

model = transferLearning.BEATsTransferLearningModel()

checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))

model.load_state_dict(checkpoint['state_dict'], strict=True)
model.eval()

def predict_main():
    while(True):
        if os.listdir(data_path) :
            data_list = os.listdir(data_path)
            data_list.sort(reverse=True)
            prob, result = predict(model, data_path)
            if result > 11:
                print(result)
                os.remove(os.path.join(data_path, data_list[0]))    
                continue
            else:
                print(result)
                os.remove(os.path.join(data_path, data_list[0]))  
                continue
        else:
            print("end")
            continue
