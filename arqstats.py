import pandas as pd 
import numpy as np
import scipy
from scipy import stats


# this class implements statistical calculations
class arqstats:

    # constructor
    def __init__(self, data):

        # change df to numpy
        if isinstance(data, pd.DataFrame):
            self.column_names = data.columns.tolist()
            self.data_np = data.to_numpy()

    def get_data(self):
        return self.data_np, self.column_names

    def calc_mean(self, var_name):
        # calculates mean
        # input [list]:    var_name is a list of the names of variable for which the mean is calculated
        # output [np array]:   mean value of var_name variable(s)

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))

        mean = np.mean(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows

        return mean

    def calc_median(self, var_name):
        # calculates median
        # input [list]:    var_name is a list of the names of variable for which the median is calculated
        # output [np array]:   median value of var_name variable(s)

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))

        median = np.median(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows

        return median


    def calc_mode(self, var_name, return_counts=False):
        # calculates mode
        # input [list]:    var_name is a list of the names of variable for which the mode is calculated
        # input [return_counts]:    if True, returns counts of the mode
        # output [np array]:   mode value of var_name variable(s)      

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))

        #mode = np.mode(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows
        mode = stats.mode(self.data_np[:,var_name_idx_list])[0][0]
        counts = stats.mode(self.data_np[:,var_name_idx_list])[1][0]

        if return_counts:
            return mode, counts
        else:
            return mode

    def calc_var(self, var_name):
        # calculates variance
        # input [list]:    var_name is a list of the names of variable for which the variance is calculated
        # output [np array]:   variance of var_name variable(s)

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))

        variance = np.var(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows

        return variance

    def calc_stdev(self, var_name):
        # calculates standard deviation
        # input [list]:    var_name is a list of the names of variable for which the standard deviation is calculated
        # output [np array]:   standard deviation of var_name variable(s)

        #var_name_idx_list = []

        #for var in var_name:
        #    var_name_idx_list.append(self.column_names.index(var))
        #stdev = np.var(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows
        
        stdev = np.sqrt(self.calc_var(var_name))
        
        return stdev

    def calc_range(self, var_name):
        # calculates range
        # input [list]:    var_name is a list of the names of variable for which the range is calculated
        # output [np array]:   standard deviation of var_name variable(s)

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))
        range_ = np.max(self.data_np[:,var_name_idx_list], axis=0) - np.min(self.data_np[:,var_name_idx_list], axis=0) # axis=0 for columns, axis=1 for rows
                
        return range_

    def calc_percentile(self, var_name, perc_):
        # calculates percentile
        # input [list]:    var_name is a list of the names of variable for which the range is calculated
        # percentile:      perc_ is the percentile that is calculated
        # output [np array]:   percentile of var_name variable(s)

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))
        percentiles_ = np.percentile(self.data_np[:,var_name_idx_list], perc_, axis=0)
                
        return percentiles_

    def calc_percentiles(self, var_name, perc_list_):
        # calculates percentiles
        # input [list]:    var_name is a list of the names of variable for which the range is calculated
        # percentile_list: perc_list_ is a list of percentiles that is calculated
        # output [np array]:   percentile of var_name variable(s)

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))
        
        percentiles_np = []
        for perc_ in perc_list_:
            percentiles_ = np.percentile(self.data_np[:,var_name_idx_list], perc_, axis=0)
            percentiles_np.append(percentiles_)
        
        percentiles_np = np.array(percentiles_np)
                
        return percentiles_np