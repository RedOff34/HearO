import torch 
from BEATs_eval import predict
import transferLearning
import sms

data_path = '/sound/'
checkpoint_path = './model/BEATs_iter3+_AS2M_10s.ckpt'

model = transferLearning.BEATsTransferLearningModel()

checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))

model.load_state_dict(checkpoint['state_dict'], strict=True)
model.eval()


while(True):
    if data_path :
        prob, result = predict(model, data_path)
        if result > 11:    
            continue
        else:
            sms()
    else:
        continue