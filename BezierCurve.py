import numpy as np
from math import factorial
from matplotlib import pyplot as plt
from matplotlib.animation import PillowWriter

""" Volevo usare il builder, ma i design pattern sono inusabili in Python...o sono scarso io """

class BezierCurve():
    def __init__(self,control_polygon=None,Points=None) -> None:
        return None

    def withControlPoints(self,number_of_points:int):
        if(number_of_points < 1):
            raise ValueError("Control points must be greater then 0. Got {x}".format(x = number_of_points))
        self.control_polygon = self.__build_control_polygon(number_of_points)
        return self
    def withBerstainBase(self):
        try:
            self.control_polygon
        except AttributeError:
            # VERY NICE
            raise SyntaxError("Must select control points first.")
        self.points_on_curve = self.__calculate_points_on_curve(self.control_polygon)
        return self

    def __build_control_polygon(self,number_of_points:int):
        '''Returns a n*2 matrix with x in col:0 and y in col:1'''
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
        return np.transpose(np.array([x,y]))
    
    def __Bernstein(self,index, grade, t):
        if(index > grade):
            raise ValueError("index must be less then n, got index: {index} and grade: {grade}".format(index=index,grade=grade))
        return factorial(grade) / (factorial(index) * factorial(grade - index)) * \
            t ** index * \
            (1 - t) ** (grade - index)

    def __calculate_points_on_curve(self,controlPolygon):
        grade = len(controlPolygon[:,0]) -1
        t_space = np.linspace(0,1,100)
        bezier_curve = np.zeros(shape=(len(t_space),2))
        for idx_t,t in enumerate(t_space):
            sum = np.zeros(shape=(1,2))
            for i in range(grade+1):
                sum = np.add(sum,controlPolygon[i,:]*self.__Bernstein(i,grade,t))
            bezier_curve[idx_t,:] = sum
        return bezier_curve

    def draw(self):
        fig = plt.figure()
        l, = plt.plot([],[],'c-')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.grid()
        plt.title("Bezier curve grade {grade}".format(grade=len(self.control_polygon[:,0])+1))
        writer = PillowWriter(fps=15)
        xpoints = []
        ypoints = []	
        with writer.saving(fig,"BezierCurve.gif",100):
            for point in self.points_on_curve:
                xpoints.append(point[0])
                ypoints.append(point[1])
                plt.plot(self.control_polygon[:,0],self.control_polygon[:,1],':rx')
                l.set_data(xpoints,ypoints)
                writer.grab_frame()
        return self



