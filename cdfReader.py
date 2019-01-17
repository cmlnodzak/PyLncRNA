import numpy as np
import sys
from collections import OrderedDict


def probesetParser(infile):
    probeSets =OrderedDict()
    with open(infile,'r') as cdf:
        for line in cdf.readlines():
            if "[Unit%*d_Block%d]" in line:
                while not line.startswith("Unit%*d"):
                    

def cdf(path,probeType = 'PM'):
    assert isinstance(path, str)
    assert isinstance(probe_type, str)

    if probeType == 'PM':
        probes = 0
    elif probeType == 'MM':
        probes = 1
    elif probeType == 'all':
        probes = 2
    else:
        raise Exception('Unrecognized probeType. Options are PM, MM, or all.')

    probeSets = OrderedDict()
    try:
        
