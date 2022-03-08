import math
import scipy.stats
from scipy import integrate

# this class implements the Continuous Normal Distribution
class normal_dist:

    # constructor
    def __init__(self, mean, stdev):

        # set the mean and the standard deviation
        self.mean = mean
        self.stdev = stdev

    def get_mean(self):
        return self.mean

    def get_stdev(self):
        return self.stdev
    

