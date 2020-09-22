## Wrapper.py

import math

class Trapper:
	
	def __init__(self,file_path_):
		self.file_path = file_path_

	def FileToPositionArray(self):
		f = open(self.file_path,'r')
		data = f.readlines()
		triangle_pos_list=[]
		for line in data:
			vertices=line.split()
			pose_array=[]
			for data in vertices:
				pos = data.split(',')
				for value in pos:
					pose_array.append(float(value))
        	#print(pose_array)
			triangle_pos_list.append(pose_array)
		return triangle_pos_list


# class triangle2DList:
# 	def __init__(self):
# 		self.List = []

# 	def appendTriangle(triangle):
# 		self.List.append(triangle)



class triangle2D:
	triangle2DList=[]
	
	def __init__(self,vertices_):
		self.vertices = vertices_
		self.area = self.getArea()
		self.meanArea = None
		self.__class__.triangle2DList.append(self)

	def getArea(self):
		area_ = abs(0.5*(self.vertices[0]*(self.vertices[3]-self.vertices[5])+
			self.vertices[2]*(self.vertices[5]-self.vertices[1])+
			self.vertices[4]*(self.vertices[1]-self.vertices[3])))
		return area_
		
	def getMean(self):
		meanArea = 0
		for thisObj in self.__class__.triangle2DList:
			meanArea += thisObj.area
		meanArea = meanArea/len(self.__class__.triangle2DList)
		self.meanArea = meanArea
		return meanArea

	def getStdDev(self):
		stdDev = 0
		for thisObj in self.__class__.triangle2DList:
			if(self.meanArea == None):
				self.getMean()
			stdDev += (thisObj.area-self.meanArea)*(thisObj.area-self.meanArea)
		stdDev = stdDev/(len(self.__class__.triangle2DList)-1)
		self.stdDevArea = stdDev
		return stdDev
		

			







