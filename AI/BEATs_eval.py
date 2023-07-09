import torch 
import torch.nn.functional as nnf
import librosa
import os

def predict(model, data_path):
    model.eval()
    with torch.no_grad():
        data_list = os.listdir(data_path)
        data_list.sort(reverse=True)
        audio_path = os.path.join(data_path, data_list[0])
        sig, sr = librosa.load(audio_path, sr= 44100, mono = True)
        sig = librosa.util.fix_length(sig, size=10*sr)
        sig_t = torch.tensor(sig)
        sig_t = sig_t.reshape(-1,10*sr)
        result = model(sig_t)
        prob = nnf.softmax(result, dim=1)
        prob = int(prob.topk(1,dim=1)[0]*100)
        result = int(result.argmax(1))
        return [prob, result]