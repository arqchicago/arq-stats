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


