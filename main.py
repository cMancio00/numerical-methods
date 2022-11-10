from BezierCurve import BezierCurve
from Control_Polygon import Control_Polygon
from matplotlib import pyplot as plt
import numpy as np
import time


def main():
	controlPolygon = Control_Polygon().withControlPoints(4)
	BezierCurve().withControlPoligon(controlPolygon).withBerstainBase().save_as_gif()


if __name__ == '__main__':
	main()