from math import factorial
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import PillowWriter
matplotlib.use('Qt5Agg')

def Bernstein(index, grade, t):
    if(index > grade):
        raise ValueError("index must be less then n, got index: {index} and grade: {grade}".format(index=index,grade=grade))
    return factorial(grade) / (factorial(index) * factorial(grade - index)) * \
           t ** index * \
           (1 - t) ** (grade - index)


def BezierCurve(controlPolygon,t_space):
    grade = len(controlPolygon[0,:]) -1
    bezier_curve = np.zeros(shape=(len(t_space),2))
    for idx_t,t in enumerate(t_space):
        sum = np.zeros(shape=(1,2))
        for i in range(grade+1):
            sum = np.add(sum,controlPolygon[:,i]*Bernstein(i,grade,t))
        bezier_curve[idx_t,:] = sum
    return bezier_curve


def build_control_polygon(number_of_points:int):
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.grid()
    gpoints = plt.ginput(number_of_points)
    x = list()
    y = list()
    for point in gpoints:    
        x.append(point[0])
        y.append(point[1])
    plt.close()  
    return np.array([x,y])

def animate_Bezier_Curve(bezier_Curve,control_polygon):
    fig = plt.figure()
    l, = plt.plot([],[],'c-')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.grid()
    plt.title("Bezier curve grade {grade}".format(grade=len(control_polygon[0,:])+1))
    writer = PillowWriter(fps=15)
    xpoints = []
    ypoints = []	
    with writer.saving(fig,"BezierCurve.gif",100):
        for point in bezier_Curve:
            xpoints.append(point[0])
            ypoints.append(point[1])
            plt.plot(control_polygon[0,:],control_polygon[1,:],':rx')
            l.set_data(xpoints,ypoints)
            writer.grab_frame()