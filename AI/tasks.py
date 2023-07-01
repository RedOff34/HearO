from __future__ import absolute_import, unicode_literals
from celery import shared_task
import sys
sys.path.append('C:/Users/Jae Ung Jung/Big_project_3_9')
import torch 
from AI.BEATs_eval import predict
from AI import transferLearning
import shutil
import requests
import os


data_path = './AI/sound/'
checkpoint_path = './AI/model/BEATs_iter3+_AS2M_10s.ckpt'

model = transferLearning.BEATsTransferLearningModel()

checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))


model.load_state_dict(checkpoint['state_dict'], strict=True)
model.eval()



@shared_task
def predict_main():
    while(True):
        if os.listdir(data_path) :
            data_list = os.listdir(data_path)
            data_list.sort(reverse=True)
            prob, result = predict(model, data_path)
            if result > 11:
                print("일반상황")
                print(data_list[0])
                print("확률: ", prob, end='')  
                print("범주: ", result)
                os.remove(os.path.join(data_path, data_list[0]))    
                continue
            else:
                print("응급상황")
                print("확률: ", prob, end='')  
                print("범주: ", result)
                file_name = data_list[0][:-4] + '_' + str(result).zfill(2) + '_' + str(prob).zfill(2)+'.wav' 
                shutil.move(os.path.join(data_path, data_list[0]), os.path.join('./media/sound_history/', data_list[0].split('_')[0], file_name))
                continue
        else:
            continue