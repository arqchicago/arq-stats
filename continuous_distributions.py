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

    def pdf(self, x):
        # calculates Probability Distribution Function P(X<x)
        # input [float x]:    x is the value for which P(X<x) is returned
        # P(X<x) = 1/sqrt(2*Pi*sd**2) * e^(-1/2 * ((x-mean)/s)**2 )
        
        p_x = (1/(2*math.pi*(self.stdev**2))**0.50) * (math.exp(-0.50*((x-self.mean)/self.stdev)**2))
        return p_x
    
    def cdf(self,x1,x2):
        pdf = lambda x: (1/(2*math.pi*(self.stdev**2))**0.50) * (math.exp(-0.50*((x-self.mean)/self.stdev)**2))
        p_x_cdf = integrate.quad(pdf, x1, x2)
        p_x_cdf = round(p_x_cdf[0], 10)
        
        return p_x_cdf
    

