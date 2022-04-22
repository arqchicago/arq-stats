import math
import scipy.stats
from scipy import integrate
from scipy.special import erfinv
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

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
    
    def cdf(self, x1):
        pdf = lambda x: (1/(2*math.pi*(self.stdev**2))**0.50) * (math.exp(-0.50*((x-self.mean)/self.stdev)**2))
        p_x_cdf = integrate.quad(pdf, -20, x1)
        p_x_cdf = round(p_x_cdf[0], 10)
        
        return p_x_cdf
    
    def cdfr(self, x1):
        p_x_cdf = self.cdf(x1)
        p_x_cdfr = 1 - p_x_cdf
        
        return p_x_cdfr
    
    def cdfb(self, x1, x2):
        pdf = lambda x: (1/(2*math.pi*(self.stdev**2))**0.50) * (math.exp(-0.50*((x-self.mean)/self.stdev)**2))
        p_x_cdf = integrate.quad(pdf, x1, x2)
        p_x_cdf = round(p_x_cdf[0], 10)
        
        return p_x_cdf
    
    def inv(self, p):
        # cdf P(Z<z) = integral{ 1/sqrt(2*Pi) * e^((-z^2)/2)  }
        # let u = z/sqrt(2)
        # then du = 1/sqrt(2) dz
        # dz = sqrt(2) * du
        # cdf P(Z<z) = integral{ sqrt(2)/sqrt(2*Pi) * e^(-u^2) du  }
        # cdf P(Z<z) = integral{ sqrt(2)*sqrt(2)/(sqrt(2*Pi)*sqrt(2)) * e^(-u^2) du  }
        # cdf P(Z<z) = 1/2 * integral{ 2/sqrt(Pi) * e^(-u^2) du  }
        # cdf P(Z<z) = (1/2) * (2/sqrt(Pi) * integral{ e^(-u^2) du  })
        # cdf P(Z<z) = (1/2) * erf(u)
        # cdf P(Z<z) = (1/2) * erf(z/sqrt(2))
        # (1/2) * erf(z/sqrt(2)) = p
        # erf(z/sqrt(2)) = 2*p
        # z = erfinv(2*p) * sqrt(2)
        # p = 1/2*(1 + math.erf(1.96/(2**0.50)))
        # p = 1/2 + 1/2 * erf(z/sqrt(2))
        # erf(z/sqrt(2)) = 2p - 1
        # z = erfinv(2p - 1) * sqrt(2)
        # x = self.mean + z * self.stdev
        
        z = erfinv(2*p - 1) * math.sqrt(2)
        x = self.mean + z * self.stdev
        return x
    
    def invr(self, p_r):
        p = 1 - p_r
        x = self.inv(p)
        return x
    
    def invm(self, p_m):
        p = 0.50 + p_m/2 
        x = self.inv(p)
        return x
    
    def draw_z_score(self, range_, x1, title=''):
        
        x_list = np.arange(-3,3,0.01)
        
        if range_ == '<':
            cond = x_list<x1
            filename = 'area_norm_z_less.png'

        #y = norm.pdf(x, self.mean, self.stdev)
        y = [self.pdf(x) for x in x_list]
        
        z_list = x_list[cond]
        z_pdf = [self.pdf(z) for z in z_list]
        plt.plot(x_list, y)
        #print(norm.pdf(z, self.mean, self.stdev))
        plt.fill_between(z_list, 0, z_pdf) #norm.pdf(z, self.mean, self.stdev))
        plt.title(title)
        plt.savefig(filename)
    
class std_normal_dist(normal_dist):
    def __init__(self):
        super().__init__(mean=0, stdev=1)