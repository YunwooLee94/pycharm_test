"""

"""
from matplotlib import pyplot as plt
import numpy as np

class Reader:

    def __init__(self, file_path_):
        self.file_path = file_path_

    def FileToPositionArray(self):
        f = open(self.file_path, 'r')
        data = f.readlines()
        triangle_pos_list = []
        for line in data:
            vertices = line.split()
            pose_array = []
            for data in vertices:
                pos = data.split(',')
                for value in pos:
                    pose_array.append(float(value))
            triangle_pos_list.append(pose_array)
        return triangle_pos_list

class c_triangle2D:
    triangle2DList = []

    def __init__(self, vertices_):
        self.vertices = vertices_
        self.area = self.getArea()
        self.meanArea = None
        self.__class__.triangle2DList.append(self)
        self.isRotated = False

    def getArea(self):
        area_ = abs(0.5 * (self.vertices[0] * (self.vertices[3] - self.vertices[5]) +
                           self.vertices[2] * (self.vertices[5] - self.vertices[1]) +
                           self.vertices[4] * (self.vertices[1] - self.vertices[3])))
        return area_

    def getMean(self):
        meanArea = 0
        for thisObj in self.__class__.triangle2DList:
            meanArea += thisObj.area
        meanArea = meanArea / len(self.__class__.triangle2DList)
        self.meanArea = meanArea
        return meanArea

    def getStdDev(self):
        stdDev = 0
        for thisObj in self.__class__.triangle2DList:
            if (self.meanArea == None):
                self.getMean()
            stdDev += (thisObj.area - self.meanArea) * (thisObj.area - self.meanArea)
        stdDev = stdDev / (len(self.__class__.triangle2DList) - 1)
        self.stdDevArea = stdDev
        return stdDev

    def drawTriangle(self):
        plt.triplot(np.array([self.vertices[0], self.vertices[2], self.vertices[4]]),
                    np.array([self.vertices[1], self.vertices[3], self.vertices[5]]))


"""
Define 2d vector class
"""


class c_vector:
    def __init__(self, numbers):
        self.x = numbers[0]
        self.y = numbers[1]

    def addVector(self, vector2):
        self.x = self.x + vector2.x
        self.y = self.y + vector2.y

    def multiply(self, matrix2):
        x_temp = matrix2.a11 * self.x + matrix2.a12 * self.y
        y_temp = matrix2.a21 * self.x + matrix2.a22 * self.y
        self.x = x_temp
        self.y = y_temp


class c_matrix:
    def __init__(self, matrix_vector):
        self.a11 = matrix_vector[0][0]
        self.a12 = matrix_vector[0][1]
        self.a21 = matrix_vector[1][0]
        self.a22 = matrix_vector[1][1]


class c_affine_transform(c_vector):
    def __init__(self, numbers):
        super().__init__(numbers)

    def affine_transform(self, matrixA, matrixB):
        self.multiply(matrixA)
        self.addVector(matrixB)
        return [self.x, self.y]