#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:36:07 2019

@author: cmlnodzak
"""

from collections import OrderedDict
from genometools import misc
from pyaffy import rma
import os
import pandas as pd
#from pybedtools import BedTool

#snps = BedTool('snps.bed.gz')  # [1]
#genes = BedTool('hg19.gff')    # [1]
#
#intergenic_snps = snps.subtract(genes)                       # [2]
#nearby = genes.closest(intergenic_snps, d=True, stream=True) # [2, 3]
#
#for gene in nearby:             # [4]
#    if int(gene[-1]) < 5000:    # [4]
#        print(gene.name)
#        
        
# data_dir: the directory in which downloaded data will be stored
data_dir = './data/'
# output_dir: the directory in which generated data will be stored
output_dir = './output/'

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

cdf_file = 'HGU133Plus2_Hs_ENSG.cdf'

misc.get_logger(verbose = False)

#sample_cel_files: collections.OrderedDict (st => str)
#        An ordered dictionary where each key/value-pair corresponds to a
#        sample. The *key* is the sample name, and the *value* is the (absolute)

sample_cel_files = OrderedDict()
try: 
    with open("celfiles.txt",'r') as cels:
        for line in cels.readlines():
            line=line.rstrip().split("\t")
            sample_cel_files[line[0]] = line[1]
except IOError:
    print('Could not open the file mapping sample name to CELs!\n')


# Perform RMA normalization over all microarrays.
genes, samples, X = rma(cdf_file, sample_cel_files)

exprMatr = pd.DataFrame(X, index=genes,columns=samples)












