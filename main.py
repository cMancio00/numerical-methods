import curves
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Qt5Agg')

def main():
	# try:
	# 	print(Bernstein(index=0,grade=1,t=1))
	# except ValueError as e:
	# 	print(str(e))
	t = np.linspace(0,1,101)
	grade = 5
	control_polygon = curves.build_control_polygon(grade+1)
	plt.xlim([0, 1])
	plt.ylim([0, 1])
	plt.plot(control_polygon[0][:],control_polygon[1][:],':r+')
	curve = curves.BezierCurve(control_polygon,grade,t)
	plt.plot(curve[:,0],curve[:,1])
	# x = list()
	# y = list()
	# for ax in t:
	# 	for i in range(grade+1):
	# 		x=control_polygon[:,i] * curves.Bernstein(i,grade,ax)
	# 		print(x)
	# 	plt.plot(x[0],x[1])



	plt.show()


if __name__ == '__main__':
	main()