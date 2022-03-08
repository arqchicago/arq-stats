import csv
import pandas as pd
from arqstats import arqstats
import continuous_distributions
import time

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
    
    stdev_age_cp = arq_data.calc_stdev(['age', 'cp'])
    print(f'Variables [age, cp] standard deviation = {stdev_age_cp}')
    
    range_age_cp = arq_data.calc_range(['age', 'cp'])
    print(f'Variables [age, cp] range = {range_age_cp}')
    
    percentile_age_cp = arq_data.calc_percentile(['age', 'cp'], 75)
    print(f'Variables [age, cp] percentile = {percentile_age_cp}')
    
    percentiles_age_cp = arq_data.calc_percentiles(['age', 'cp'], [50, 75])
    print(f'Variables [age, cp] percentiles = \n{percentiles_age_cp}')



    # Normal Distribution
    mean = 0 
    sd = 1
    norm_dist = continuous_distributions.normal_dist(mean, sd)
    print(f'Normal Distribution:   mean={norm_dist.get_mean()},  standard deviation={norm_dist.get_stdev()}')

    