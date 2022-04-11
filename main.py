import csv
import pandas as pd
from arqstats import arqstats
import continuous_distributions
from continuous_distributions import normal_dist, std_normal_dist
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
    mean = 20 
    sd = 2
    norm_dist = normal_dist(mean, sd)
    print(f'\nNormal Distribution:   mean={norm_dist.get_mean()},  standard deviation={norm_dist.get_stdev()}')

    print(f'PDF   P(x=20) = {norm_dist.pdf(20)}')
    print(f'PDF   P(x=23.92) = {norm_dist.pdf(23.92)}')
    print(f'CDF   P(x<20) = {norm_dist.cdf(20)}')
    print(f'CDF   P(x<23.92) = {norm_dist.cdf(23.92)}')
    print(f'CDF   P(x>20) = {norm_dist.cdfr(20)}')
    print(f'CDF   P(x>23.92) = {norm_dist.cdfr(23.92)}')
    print(f'CDF   P(20<x<23.92) = {norm_dist.cdfb(20, 23.92)}')
    print(f'CDF   P(16.08<x<23.92) = {norm_dist.cdfb(16.08, 23.92)}')
    print(f'CDF   x where P(X<x) = 0.9750,   x = {norm_dist.inv(0.975)}')
    print(f'CDF   x where P(X<x) = 0.0250,   x = {norm_dist.inv(0.025)}')
    print(f'CDF   x where P(X>x) = 0.9750,   x = {norm_dist.invr(0.975)}')
    print(f'CDF   x where P(X>x) = 0.0250,   x = {norm_dist.invr(0.025)}')
    print(f'CDF   x where P(-x<X<x) = 0.90,   x = {norm_dist.invm(0.90)}')
    print(f'CDF   x where P(-x<X<x) = 0.95,   x = {norm_dist.invm(0.95)}')
    print(f'CDF   x where P(-x<X<x) = 0.99,   x = {norm_dist.invm(0.99)}')

    
    # Std Normal Distribution
    std_norm_dist = std_normal_dist()
    print(f'\nStd Normal Distribution:   mean={std_norm_dist.get_mean()},  standard deviation={std_norm_dist.get_stdev()}')

    print(f'PDF   P(x=0) = {std_norm_dist.pdf(0)}')
    print(f'PDF   P(x=1.96) = {std_norm_dist.pdf(1.96)}')
    print(f'CDF   P(x<0) = {std_norm_dist.cdf(0)}')
    print(f'CDF   P(x<1.96) = {std_norm_dist.cdf(1.96)}')
    print(f'CDF   P(x>0) = {std_norm_dist.cdfr(0)}')
    print(f'CDF   P(x>1.96) = {std_norm_dist.cdfr(1.96)}')
    print(f'CDF   P(0<x<1.96) = {std_norm_dist.cdfb(0, 1.96)}')
    print(f'CDF   P(-1.96<x<1.96) = {std_norm_dist.cdfb(-1.96, 1.96)}')
    print(f'CDF   x where P(X<x) = 0.9750,   x = {std_norm_dist.inv(0.975)}')
    print(f'CDF   x where P(X<x) = 0.0250,   x = {std_norm_dist.inv(0.025)}')
    print(f'CDF   x where P(X>x) = 0.9750,   x = {std_norm_dist.invr(0.975)}')
    print(f'CDF   x where P(X>x) = 0.0250,   x = {std_norm_dist.invr(0.025)}')
    print(f'CDF   x where P(-x<X<x) = 0.90,   x = {std_norm_dist.invm(0.90)}')
    print(f'CDF   x where P(-x<X<x) = 0.95,   x = {std_norm_dist.invm(0.95)}')
    print(f'CDF   x where P(-x<X<x) = 0.99,   x = {std_norm_dist.invm(0.99)}')
