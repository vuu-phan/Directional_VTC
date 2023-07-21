# name: visualizer.py
# description: visualize CoP and directional VTC time series
# author: Vu Phan
# date: 2023/07/21


import matplotlib.pyplot as plt 


def plot_cop(cop, bos = None, xlims = None, ylims = None):
	""" Plot CoP data (and BOS)

	Params: 
		cop: anterior-posterior and medio-lateral CoP data | EasyDict of np.array
		bos: base of support | EasyDict of list
		xlims, ylims: limits of x and y axis | list of int

	Returns:
		No return but plotting data
	"""
	fig, ax = plt.subplots(figsize = (6, 4), dpi = 100)
	ax.plot(cop.x, cop.y, linewidth = 0.8, color = '#595F72', alpha = 0.4)

	if bos == None:
		pass
	else:
		ax.plot([bos.A[0], bos.B[0], bos.C[0], bos.D[0], bos.A[0]], 
				[bos.A[1], bos.B[1], bos.C[1], bos.D[1], bos.A[1]], color = '#2B303A')

	if xlims == None:
		pass
	else:
		ax.set_xlim(xlims)

	if ylims == None:
		pass
	else:
		ax.set_ylim(ylims)

	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	ax.set_aspect('equal', adjustable='box')

	plt.show()


def plot_ts(time, ts, xlims = None, ylims = None, thres = None):
	""" Plot VTC or BC time-series

	Params:
		ts: time-series of VTC or BC | np.array
		xlims, ylims: limits of x and y axis | list of int
		thres: threshold used for switch rate extraction | float

	Returns:
		No return but plotting data
	"""
	fig, ax = plt.subplots(figsize = (6, 4), dpi = 100)
	ax.plot(time, ts, color = '#595F72', linewidth = 1.5)

	if thres == None:
		pass
	else:
		ax.hlines(thres, time[0], time[-1], linestyles = 'dashed', color = '#C7CEDB')

	if xlims == None:
		pass
	else:
		ax.set_xlim(xlims)

	if ylims == None:
		pass
	else:
		ax.set_ylim(ylims)

	ax.spines['left'].set_position(('outward', 8))
	ax.spines['bottom'].set_position(('outward', 5))
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)

	plt.show()
