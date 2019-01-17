import numpy as np
import pandas as pd
import scipy.stats
from math import floor, sqrt

def correct(matr):
    """ Function to perform background correction for RMA normalization of affymetrix arrays
    Parameter 
    ===============
    matr: a matrix of microarray intesity values.
    """
    assert isinstance(matr, pd.DataFrame)
    # remove missing data, use binning to estimate mean
    for k in range(matr.shape[1]):
        m = isnan(matr[:,k])
        j = m[~m,k]
        bins = 100
        lowerbound = np.amin(j)
        upperbound = np.percentile(j,75)
        width = max(floor(upper-lower)/bins),1.0)
        edge = np.arange(lower,upper,width)
        binNum = edge.size -1
        
        bin = np.digitize(y, bins = edge) - 1
        bin = bin[bin < binNum]
        binCount = np.bincount(bin)
        amax = np.argmax(binCount)
        mu = lower + (amax + 0.5) * width
        j_low = j[j < mu]
        sigma = sqrt(np.sum(j_low - mu, 2.0) / (j_low.size -1))
        sigma *= sqrt(2.0)
        alpha = 0.03
        a = j - mu * sqrt(sigma)
        adjust = a + sigma * np.exp(norm.logpdf(a /sigma) - norm.logcdf(a / sigma))
        matr[~m,j] = adjust
    return matr
