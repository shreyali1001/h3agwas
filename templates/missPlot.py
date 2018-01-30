#!/usr/bin/env python3
#Load SNP frequency file and generate histogram

import pandas as   pd
import numpy  as np
import sys
from matplotlib import use
use('Agg')
import argparse
import matplotlib.pyplot as plt
import sys

def parseArguments():
    if len(sys.argv)<=1:
        sys.argv="snpmissPlot.py $input $label $output".split()
    parser=argparse.ArgumentParser()
    parser.add_argument('input', type=str, metavar='input'),
    parser.add_argument('label', type=str, metavar='label'),
    parser.add_argument('output', type=str, metavar='output'),
    args = parser.parse_args()
    return args

args = parseArguments()

data = pd.read_csv(args.input,delim_whitespace=True)

fig,ax = plt.subplots()
miss = data["F_MISS"]
big = min(miss.mean()+2*miss.std(),miss.nlargest(4).iloc[3])
miss = np.sort(miss[miss<big])
n = np.arange(1,len(miss)+1) / np.float(len(miss))
ax.step(miss,n)
ax.set_xlabel("Missingness")
ax.set_ylabel("Proportion of %s"%args.label)
ax.set_title("Cumulative proportion of  %s with given missingness"%args.label)
fig.tight_layout()
plt.savefig(args.output)
