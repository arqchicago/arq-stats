import math
import scipy.stats
from scipy import integrate
from scipy.special import erfinv
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

# this class implements the Discrete Poisson Distribution
class poisson_dist:

    # constructor
    def __init__(self, lambda_):

        # set the lambda
        self.lambda_ = lambda_

    def get_lambda(self):
        return self.lambda_

    def prob(self, k):
        # prob(K=k) = lambda^l * e^(-1) / k!
        prob_ = self.lambda_ * math.exp(-1) / math.factorial(k)
        
        return prob_