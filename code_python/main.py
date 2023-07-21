# name: main.py
# description: directional VTC calculation
# author: Vu Phan
# date: 2023/07/21


import pandas as pd 
import numpy as np 

from easydict import EasyDict
from vtc_utils import *
import visualizer


# Constants
fs = 2000 # Hz

# Boundary
# YOU NEED TO MEASURE BOS OF YOUR PARTICIPANT AND ENTER IT HERE -->
bos   = EasyDict()
bos.A = [10, -10]
bos.B = [15, 20]
bos.C = [-15, 20]
bos.D = [-10, -10]
# <--- YOU NEED TO MEASURE BOS OF YOUR PARTICIPANT AND ENTER IT HERE

# Get CoP data
dt = pd.read_csv('..\\data\\sample_cop.csv')
dt = dt.astype(float)

cop   = EasyDict()
cop.x = dt['COPx'].to_numpy()
cop.y = dt['COPy'].to_numpy()
time  = dt['Time'].to_numpy()

# Obtain VTC time series
vtc_s, bc_s = get_vtc_series(cop, bos, fs)

# Calculate directional VTC outcomes
outcomes = get_vtc_outcomes(vtc_s, bc_s, fs)

print('2D VTC mean = ' + str(round(outcomes[0], 2)) + ' (s)')
print('AP VTC mean = ' + str(round(outcomes[1], 2)) + ' (s)')
print('ML VTC mean = ' + str(round(outcomes[2], 2)) + ' (s)')
print('AP BC = ' + str(round(outcomes[3], 2)) + ' (%)')
print('ML BC = ' + str(round(outcomes[4], 2)) + ' (%)')
print('Switching rate = ' + str(round(outcomes[5], 2)) + ' (Hz)')

# Plot CoP data
visualizer.plot_cop(cop, bos)

# Plot time-series data
visualizer.plot_ts(time[2::], vtc_s, thres = outcomes[-1])
visualizer.plot_ts(time[2::], bc_s)
