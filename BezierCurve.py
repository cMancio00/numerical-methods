import numpy as np
from math import factorial
from matplotlib import pyplot as plt
from Control_Polygon import Control_Polygon
from matplotlib.animation import PillowWriter
import os
from datetime import datetime

""" Volevo usare il builder, ma i design pattern sono inusabili in Python...o sono scarso io """

class BezierCurve():
    def __init__(self,control_polygon=None,Points=None) -> None:
        return None

    def withControlPoligon(self,control_polygon:Control_Polygon):
        self.control_polygon = control_polygon
        return self
        
    def withBerstainBase(self):
        try:
            self.control_polygon
        except AttributeError:
            # VERY NICE
            raise SyntaxError("Must select control points first.")
        self.points_on_curve = self.__calculate_points_on_curve(self.control_polygon)
        return self
    
    def __Bernstein(self,index, grade, t):
        if(index > grade):
            raise ValueError("index must be less then n, got index: {index} and grade: {grade}".format(index=index,grade=grade))
        return factorial(grade) / (factorial(index) * factorial(grade - index)) * \
            t ** index * \
            (1 - t) ** (grade - index)

    def __calculate_points_on_curve(self,controlPolygon:Control_Polygon):
        grade = len(controlPolygon.get_x()) -1
        t_space = np.linspace(0,1,100)
        bezier_curve = np.zeros(shape=(len(t_space),2))
        for idx_t,t in enumerate(t_space):
            sum = np.zeros(shape=(1,2))
            for i in range(grade+1):
                sum = np.add(sum,controlPolygon.get_point(i)*self.__Bernstein(i,grade,t))
            bezier_curve[idx_t,:] = sum
        return bezier_curve

    def get_x(self):
        return self.points_on_curve[:,0]
    
    def get_y(self):
        return self.points_on_curve[:,1]

    def save_as_gif(self):
        fig = plt.figure()
        l, = plt.plot([],[],'c-')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.grid()
        plt.title("Bezier curve grade {grade}".format(grade=len(self.control_polygon.get_x())+1))
        writer = PillowWriter(fps=15)
        xpoints = []
        ypoints = []
        try:
            os.mkdir("gifs")
        except OSError:
            print('Directory already created')	
        with writer.saving(fig,"gifs/BezierCurve_{date}.gif".format(date = datetime.now()),100):
            for point in self.points_on_curve:
                xpoints.append(point[0])
                ypoints.append(point[1])
                plt.plot(self.control_polygon.get_x(),self.control_polygon.get_y(),':rx')
                l.set_data(xpoints,ypoints)
                writer.grab_frame()
        return self

    def draw(self):
        plt.ion()
        plt.show()
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.grid()
        plt.title("Bezier curve grade {grade}".format(grade=len(self.control_polygon.get_x())+1))
        xpoints = []
        ypoints = []
        plt.plot(self.control_polygon.get_x(),self.control_polygon.get_y(),':rx',label='Control Poligon')
        plt.plot(0,0,'c-',label='Bezier curve')
        plt.legend(loc="upper left")
        
        for point in self.points_on_curve:
            xpoints.append(point[0])
            ypoints.append(point[1])
            plt.plot(xpoints,ypoints,'c-')
            plt.draw()
            plt.pause(0.01)
        plt.ioff()
        plt.show()
        return self



