from math import factorial
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Qt5Agg')

def Bernstein(index, grade, t):
    if(index > grade):
        raise ValueError("index must be less then n, got index: {index} and grade: {grade}".format(index=index,grade=grade))
    return factorial(grade) / (factorial(index) * factorial(grade - index)) * \
           t ** index * \
           (1 - t) ** (grade - index)


def BezierCurve(controlPolygon,grade,t_space):
    print(controlPolygon)
    curve = np.zeros(shape=(len(t_space),2))
    x = 0
    for t in t_space:
        sum = np.zeros(shape=(1,2))
        for i in range(grade+1):
            sum = np.add(sum,controlPolygon[:,i]*Bernstein(i,grade,t_space[x]))
        curve[x,:] = sum
        x = x+1
    print(curve.shape)
    print(curve)
    return curve


def build_control_polygon(number_of_points:int):
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    gpoints = plt.ginput(number_of_points)
    x = list()
    y = list()
    for point in gpoints:    
        x.append(point[0])
        y.append(point[1])
    plt.close()    
    return np.array([x,y])