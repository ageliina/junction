#!/usr/bin/env python2.7
# coding: utf-8

# Author: Akke Viitanen

# Usage: ./combine.py olgaTRR.csv olgaRR.csv 

# Imports
from sys import argv
import numpy as np
import matplotlib.pyplot as plt

# Function defs
"""Read the .csv files fname1 and fname2, return (T, RR)"""
def read_data(fname1, fname2):

    T_data = np.loadtxt(fname1)
    RRs = np.loadtxt(fname2)

    Ts = np.array([])
    Rs = np.array([])

    for i in range(len(RRs)): 

        Ts = np.append(Ts, (T_data[i] + T_data[i+1]) / 2)
        Rs = np.append(Rs, RRs[i])

    return T_data, Ts, Rs

def get_std(start, stop, Ts, Rs):
    
    relevant = (Ts >= start) * (Ts <= stop)
    return np.mean(Rs[relevant])


# Main
if __name__=="__main__":

    T_data, Ts, Rs = read_data(argv[1], argv[2])

    stds = np.array([])
    t_stds = np.array([])
    for i in range(7):

        start = i * 1000
        stop = start + 1000
        
        stds = np.append(stds, get_std(start, stop, Ts, Rs))
        t_stds = np.append(t_stds, (start + stop)/2 )

    mean = np.mean(stds)

    bpms = [] 
    for R in Rs:
        bpms.append(60. / R)

    plt.subplot(311)

    plt.title("WHAT IS MY HEART RATE . C O M")
    plt.plot(Ts, Rs, 'r.', markersize=2.0)
    ax = plt.gca()

    plt.subplot(312)
    plt.plot(Ts, bpms, 'b.', markersize=2.0)

    plt.subplot(313, sharex=ax)
    lo_performance = stds <= mean
    hi_performance = stds > mean
    plt.title("PERFORMANCE HISTORY")
    plt.plot(t_stds[lo_performance], stds[lo_performance], 'r.', markersize=20, label="BAD")
    plt.plot(t_stds[hi_performance], stds[hi_performance], 'g.', markersize=20, label="GOOD")
    plt.plot([min(t_stds), max(t_stds)], [mean, mean], 'k--')

    plt.legend()


    plt.show()
