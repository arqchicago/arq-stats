import pandas as pd 
import numpy as np
import scipy
from scipy import stats


# this class implements breadth first search algorithm
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
        # output [np array]:   mean value of var_name variable      

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))

        mean = np.mean(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows

        return mean

    def calc_median(self, var_name):
        # calculates median
        # input [list]:    var_name is a list of the names of variable for which the median is calculated
        # output [np array]:   median value of var_name variable      

        var_name_idx_list = []

        for var in var_name:
            var_name_idx_list.append(self.column_names.index(var))

        median = np.median(self.data_np[:,var_name_idx_list], axis=0)  # axis=0 for columns, axis=1 for rows

        return median