# Directional Virtual Time-to-Contact: A New Measure for Investigating Temporal, Spatial, and Control Aspects of Postural Balance Control

This repository contains the implementation of customized functions for directional virtual time-to-contact (VTC). We support both MATLAB (see `code_matlab` folder) and Python (see `code_python` folder) users. Sample data are also included. You can preserve the same directory tree (below) to directly run the code in your local machine:

```
$ Directory tree
.
├── data\
│   ├── sample_cop.csv
├── code_matlab\
│   ├── main.m
│   ├── vtc_utils.m
│   └── visualizer.m
└── code_python\
    ├── main.py
    ├── vtc_utils.py
    └── visualizer.py
```

See [our publication](https://www.sciencedirect.com/science/article/pii/S0021929022004699) on the *Journal of Biomechanics* for more detail of the method and testing scenarios. 

## Importance before Using the Code
We assume that you already did pre-processing steps (e.g., filling missing gaps, filtering, etc.) on your data before using the code. 

## Preparing Your Data
The calculation of VTC requires:
- **Center-of-pressure (CoP)** - measured by force platform(s). We typically use net CoP displacements for the VTC calculation. If you have CoP data under each foot, you can obtain the net CoP based on the following equation ([Winter](https://www.sciencedirect.com/science/article/pii/0966636296828499), 1995). 

$$COP_{net} = COP_{l} \times {R_{vl} \over R_{vl} + R_{vr}} + COP_{r} \times {R_{vr} \over R_{vl} + R_{vr}}$$

where, $COP_{l}$ and $R_{vl}$ is the COP and vertical ground reaction force under the *left* foot, respectively; while $COP_{r}$ and $R_{vr}$ is, respectively, the COP and vertical ground reaction force under the *right* foot.

- **Boundary** or **base of support (BoS)** - either measured by a marker-based motion capture system or other means. We use a trapezoid (or its special case, a rectangle) fitting participant's feet as the BoS. Future updates will address more complex shapes of the BoS or use functional limit of stability for the VTC calculation.

![figure [exercise]: COP and BOS](figures/cop_bos.png)

## Using the MATLAB Code
*(See this if you are using MATLAB for your analysis)*

Coming soon ...


## Using the Python Code
*(See this if you are using Python for your analysis)*

```python
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
```

## Citation

If you find the code helpful for your work, please consider citing [our paper](https://www.sciencedirect.com/science/article/pii/S0021929022004699):
```
@article{PHAN2023111428,
title = {Directional virtual time-to-contact: A new measure for investigating temporal, spatial, and control aspects of postural balance control},
journal = {Journal of Biomechanics},
volume = {146},
pages = {111428},
year = {2023},
issn = {0021-9290},
doi = {https://doi.org/10.1016/j.jbiomech.2022.111428},
url = {https://www.sciencedirect.com/science/article/pii/S0021929022004699},
author = {Vu Phan and Daniel S. Peterson and Hyunglae Lee},
keywords = {Biomechanics, Standing balance, Postural balance, Postural stability, Balance stability},
abstract = {Virtual time-to-contact (VTC) is a promising approach for investigating postural balance control. However, current VTC calculation approaches are limited as they (1) cannot be used to evaluate directional components of balance, and (2) only assess a single, temporal aspect of balance control. This study introduces a new approach for VTC calculation, namely directional VTC, expanding VTC to assess temporal, spatial, and control aspects of balance. Three case studies were conducted across varying populations and conditions as a proof-of-concept of the presented method. The first study examined quiet stance on a firm surface in people with Parkinson’s disease (PD; n = 10) in comparison to their healthy peers (n = 10). The second and third studies assessed balance control of healthy individuals under challenging environments. Ten healthy individuals participated in standing tasks on compliant ground surfaces, while another ten on oscillatory ground surfaces, all simulated by a dual-axis robotic platform. Preliminary results not only provided a closer look at balance control with multiple aspects, including temporal, spatial, and control aspects, but also showed how different aspects of balance changed due to neurological diseases (Case Study I) or challenging standing grounds (Case Studies II and III). This study advances our understanding of posture biomechanics and its clinical applications.}
}
```

