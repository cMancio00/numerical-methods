from BezierCurve import BezierCurve
from Control_Polygon import Control_Polygon
from matplotlib import pyplot as plt
import numpy as np
import time


def main():
	controlPolygon = Control_Polygon().withControlPoints(5)
	
	curve = BezierCurve().withControlPoligon(controlPolygon).withBerstainBase().draw()
	curve.control_polygon.changeControlPoint(1)
	curve.withBerstainBase().draw()


if __name__ == '__main__':
	main()