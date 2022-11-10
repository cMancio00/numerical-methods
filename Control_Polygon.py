import numpy as np
from matplotlib import pyplot as plt

class Control_Polygon():
    def __init__(self) -> None:
        return None

    def withControlPoints(self,number_of_points:int):
        if(number_of_points < 1):
            raise ValueError("Control points must be greater then 0. Got {x}".format(x = number_of_points))
        self.control_points = self.__build_control_polygon(number_of_points)
        return self

    def get_x(self):
        return self.control_points[:,0]
    
    def get_y(self):
        return self.control_points[:,1]

    def get_point(self,index:int):
        return self.control_points[index,:]

    def changeControlPoint(self,point_to_change:int):
        if(point_to_change < 0 or point_to_change > len(self.get_x()) - 1):
            raise ValueError("Control point do not exist, toal control points: {total}".format(total = len(self.get_x())))
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.grid()
        plt.plot(self.get_x(),self.get_y(),':rx')
        gpoint = plt.ginput(1)
        plt.close()
        self.control_points[point_to_change] = [gpoint[0][0],gpoint[0][1]]
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