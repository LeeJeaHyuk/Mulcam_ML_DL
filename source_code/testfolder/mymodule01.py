import pandas as pd
from datetime import datetime
import os

class Mytest:

    def __init__(self,model_name,best_params,best_score_):
        self.now = datetime.now()
        self.model_name = model_name
        self.best_params = best_params
        self.best_score_ = best_score_
            
    def paramsTocsv(self):
        now = self.now
        model_name = self.model_name
        best_params = self.best_params
        best_score_ = self.best_score_
        # 폴더가 없으면 생성 있으면 통과
        try:
            if not os.path.exists('modeldata'):
                os.makedirs('modeldata')
        except OSError:
            print ('Error: Creating directory. modeldata')
        
        # 파일 경로
        file_path = './modeldata/' + model_name + '.csv'
        # 시간 불러오기
        date =  now.strftime('%Y-%m-%d %H:%M:%S')
        
        # 파일이 없으면 생성 있으면 불러오기
        if os.path.isfile('./modeldata/' + model_name + '.csv'): # 파일 존재
            df_exist = pd.read_csv(file_path)
            new_score_date = pd.DataFrame([{'date':date,'best_score':best_score_}])
            new_param=pd.DataFrame([best_params])
            
            df_new = pd.concat([new_score_date,new_param],axis=1)
            df = pd.concat([df_exist,df_new],axis=0)
            df.to_csv(file_path, index=False)
            
        else: # 파일 존재하지 않음
            df_score_date = pd.DataFrame([{'date':date,'best_score':best_score_}]) #시간 + score 데이터
            df_param=pd.DataFrame([best_params])
            df = pd.concat([df_score_date,df_param],axis=1)
            df.to_csv(file_path, index=False)
        
        return