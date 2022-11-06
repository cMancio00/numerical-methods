import curves
import numpy as np


def main():	
	t = np.linspace(0,1,100)
	n_control_points = 4
	control_polygon = curves.build_control_polygon(n_control_points)
	curve = curves.BezierCurve(control_polygon,t)
	curves.animate_Bezier_Curve(curve,control_polygon)

if __name__ == '__main__':
	main()