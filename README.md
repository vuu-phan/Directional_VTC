# Directional Virtual Time-to-Contact: A New Measure for Investigating Temporal, Spatial, and Control Aspects of Postural Balance Control

This repository contains the implementation of customized functions for directional virtual time-to-contact (VTC). We support both MATLAB (see `matlab` folder) and Python (see `python` folder) users. Please find the detailed instruction to use the code below, depending on which programming language you are using.

See [our publication](https://www.sciencedirect.com/science/article/pii/S0021929022004699) for more detail of the method and testing scenarios. 

## Importance before Using the Code
In the current version, we only support VTC calculation, and assume that you already did data pre-processing steps (e.g., filling missing gaps, filtering, etc.) by yourself before using our code. If your data happened to have missing samples or other issues, you may get errors.

## Preparing Your Data
The calculation of VTC requires:
- Center-of-pressure (CoP) - measured by force platform(s). We typically use net CoP displacements for the VTC calculation. If you have CoP data under each foot, you can obtain the net CoP based on this past paper by [Winter](https://www.sciencedirect.com/science/article/pii/0966636296828499). 
- Boundary or base of support (BoS) - either measured by a marker-based motion capture system or other means. In this work, we assumed the BoS is a trapezoid fitting participant's feet. The code also works for rectangles. Future updates should address more complex shapes of the BoS or use functional limit of stability for the VTC calculation.

## Formatting Your Data
### Center-of-pressure (CoP)

Since different instruments can be used to measure center-of-pressure (CoP) displacements, formatting data is necessary. In our implementation, we formatted our CoP data as `[N x 2]` arrays, where N is the number of samples and 2 columns store CoP displacements in the medio-lateral (i.e., ML CoP) and anterior-posterior (AP CoP) directions. Find `sample_data.csv` in the folder `data` for references.

### Base of support (BoS)

As mentioned, the BoS is a trapezoid fitting the participant's feet. We define this trapezoid by its four vertices `A`, `B`, `C`, and `D` as shown in the figure below. Each vertex is a `[2 x 1]` array containing its x- and y-positions. Find `sample_bos.csv` in the folder `data` for references.

- `EXAMPLE IMAGE OF A BOS - coming soon ...`

## Using the MATLAB Code
*(See this if you are using MATLAB for your analysis)*

Coming soon ...


## Using the Python Code
*(See this if you are using Python for your analysis)*

Coming soon ...

## Additional Notes

Coming soon ...

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

