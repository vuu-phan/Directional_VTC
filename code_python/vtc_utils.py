# name: vtc_utils.py
# description: Functions for calculating directional virtual time-to-contact
# author: Vu Phan
# date: 2023/07/21


import numpy as np 
from tqdm import tqdm
from scipy.signal import find_peaks


# Utils
def get_vtc(r, v, a, vt1, vt2):
	""" Get time to contact at a specific segment (of the boundary) at an instant time

	Params:
		r: instant position (rx, ry) of the CoP | list of 2 float
		v: instant velocity (vx, vy) of the CoP | list of 2 float
		a: instant velocity (ax, ay) of the CoP | list of 2 float
		vt1: 1st vertex (x, y) of the boundary segment | list of 2 float
		vt2: 2nd vertex (x, y) of the boundary segment | list of 2 float

	Returns
		tau: time to contact at an instant time (s) | float
	"""
	A_VERY_LARGE_NUMBER = 999

	tau = A_VERY_LARGE_NUMBER

	rx = r[0]
	ry = r[1]
	vx = v[0]
	vy = v[1]
	ax = a[0]
	ay = a[1]
	x1 = vt1[0]
	y1 = vt1[1]
	x2 = vt2[0]
	y2 = vt2[1]

	if x2 == x1:
		A = ax/2.0
		B = vx
		C = rx - x1
	else:
		s = (y2 - y1)/(x2 - x1)
		A = (ay - s*ax)/2.0
		B = (vy - s*vx)
		C = ((ry - y1) - s*(rx - x1))

	p   = [A, B, C]
	rts = np.roots(p)
	for rt in rts:
		if (rt > 0) and (isinstance(rt, complex) == False):
			if tau > rt:
				tau = rt 
			else:
				pass
		else:
			pass

	return tau


def get_vtc_series(cop, bos, fs):
	""" Get virtual time-to-contact (VTC) and boundary contact (BC) time series

	Params:
		cop: anterior-posterior and medio-lateral CoP data | EasyDict of np.array
		bos: base of support | EasyDict of list
		fs: sampling rate (Hz) | int/float

	Returns:
		vtc_s: VTC time series | np.array
		bc_s: BC time series | np.array
	"""
	A_VERY_LARGE_NUMBER = 999

	ts = 1.0/fs 
	rx = cop.x 
	ry = cop.y 
	vx = np.diff(rx)/ts
	vy = np.diff(ry)/ts
	ax = np.diff(vx)/ts
	ay = np.diff(vy)/ts

	s_size = len(ax)
	vtc_s  = A_VERY_LARGE_NUMBER*np.ones(s_size)
	bc_s   = A_VERY_LARGE_NUMBER*np.ones(s_size)

	print('* Start the VTC calculation')
	for i in tqdm(range(s_size)):
		r = [rx[i+2], ry[i+2]]
		v = [vx[i+1], vy[i+1]]
		a = [ax[i], ay[i]]
		tau_AB = get_vtc(r, v, a, bos.A, bos.B)
		tau_BC = get_vtc(r, v, a, bos.B, bos.C)
		tau_CD = get_vtc(r, v, a, bos.C, bos.D)
		tau_DA = get_vtc(r, v, a, bos.D, bos.A)

		all_tau  = np.array([tau_AB, tau_BC, tau_CD, tau_DA])
		vtc_s[i] = np.min(all_tau)
		bc_s[i]  = np.where(all_tau == np.min(all_tau))[0][0]%2
	
	return vtc_s, bc_s


def get_vtc_outcomes(vtc_s, bc_s, fs, sw_thres = None):
	""" Obtain directional VTC measures

	Params:
		vtc_s: time-series of VTC | np.array
		bc_s: time-series of BC | np.array
		sw_thres: threshold for calculating switching rate | float

	Returns:
		outcomes: set of directional VTC measures | list of float
	"""
	DIR_Y = 1
	DIR_X = 0

	num_samples = len(vtc_s)

	id_y = list(np.where(bc_s == DIR_Y)[0])
	id_x = list(np.where(bc_s == DIR_X)[0])

	vtc_2d = np.mean(vtc_s)
	vtc_y  = np.mean(vtc_s[id_y])
	vtc_x  = np.mean(vtc_s[id_x])

	bc_y = len(id_y)*100.0/num_samples
	bc_x = len(id_x)*100.0/num_samples

	if sw_thres == None:
		threshold = np.mean(vtc_s) + 3*np.std(vtc_s)
	else:
		threshold = sw_thres
	peak_id, _ = find_peaks(vtc_s)
	peaks      = vtc_s[peak_id]
	count_id   = np.where(peaks >= threshold)[0]
	count      = len(count_id)
	sr         = count*fs/num_samples

	outcomes = [vtc_2d, vtc_y, vtc_x, bc_y, bc_x, sr]
	
	return outcomes

