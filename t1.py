# -*- coding: utf-8 -*-

import numpy
import random

e_End = 9
e_Trap = 3
e_Avatar = 1
e_Disable = 8
class XEvn:
	weight = 10
	height = 5
	trapNum = 10
	
	def __init__(self):
		self.data = numpy.zeros((self.weight,self.height))
		randomVec = [i for i in range(self.weight*self.height)]
		random.shuffle(randomVec)
		#print(randomVec)
		
		index = randomVec.pop()
		self.data[index/self.height][index%self.height] = e_End
		index = randomVec.pop()
		self.data[index/self.height][index%self.height] = e_Avatar
		
		for i in range(self.trapNum):
			index = randomVec.pop()
			self.data[index/self.height][index%self.height] = e_Disable
		
				
	def show(self):
		print(self.data)		


evn = XEvn()
evn.show()






