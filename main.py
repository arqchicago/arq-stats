import csv
import pandas as pd
from arqstats import arqstats

if __name__ == "__main__":

    #----  reading data
    heart_df = pd.read_csv('data\\heart2.csv')
    rows, cols = heart_df.shape
    print(f'> data rows = {rows}  data cols = {cols}')
    
    arq_data = arqstats(heart_df)
    arq_data_print = arq_data.get_data()
    print(arq_data_print)
    
    mean_age = arq_data.calc_mean(['age'])
    print(mean_age)
    
    mean_age_cp = arq_data.calc_mean(['age', 'cp'])
    print(f'Variables [age, cp] mean = {mean_age_cp}')
    
    median_age_cp = arq_data.calc_median(['age', 'cp'])
    print(f'Variables [age, cp] median = {median_age_cp}')

    mode_age_cp = arq_data.calc_mode(['age', 'cp'])
    print(f'Variables [age, cp] mode = {mode_age_cp}')
    
    var_age_cp = arq_data.calc_var(['age', 'cp'])
    print(f'Variables [age, cp] variance = {var_age_cp}')