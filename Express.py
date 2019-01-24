from collections import OrderedDict
from genometools import misc
from pyaffy import rma
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


## set up directories
data_dir = '/nobackup/shilab/Data/StJude/Leukemia_Subtypes/'
output_dir = './Expression'

if not os.path.isdir(ourput_dir):
    os.mkdir(output_dir)


misc.get_logger(verbose = False)

#TODO: make sure sampleList file is correct.
#sampleList = "/nobackup/shilab/Data/StJude/Leukemia_Subtypes/sampleList.txt"

with open(sampleList, 'r') as samp:
    for line in samp.readlines():
        line = line.rstrip().split("\t")
        sample_cel_files.update({line[0] : line[1])

sample_cel_files = OrderedDict([])

genes, samples, X = rma(cdf_file, sample_cel_files)

