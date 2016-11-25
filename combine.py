#!/usr/bin/env python2.7
# coding: utf-8

# Author: Akke Viitanen

# Usage: ./combine.py olgaTRR.csv olgaRR.csv 

# Imports
from sys import argv
import numpy as np
import matplotlib.pyplot as plt

# Main
if __name__=="__main__":
    data1 = np.loadtxt(argv[1])
    data2 = np.loadtxt(argv[2])

    Ts = []
    RRs = []

    for i in range(len(data2)): 
        if i%1000 != 0:
            continue

        print(i)

        T = (data1[i] + data1[i+1]) / 2
        RR = data2[i]

        Ts.append(T)
        RRs.append(RRs)

    plt.plot(Ts, RRs)
    plt.show()
