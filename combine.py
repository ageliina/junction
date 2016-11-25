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

    T_data = np.loadtxt(argv[1])
    RRs = np.loadtxt(argv[2])

    Ts = []
    Rs = []

    for i in range(len(RRs)): 

        Ts.append((T_data[i] + T_data[i+1]) / 2)
        Rs.append(RRs[i])


    plt.plot(Ts, Rs)
    plt.show()
