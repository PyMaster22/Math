from rational import Rational
from utils import max
class Poly:
	"""A polynomial class."""
	def __init__(self,coefficients):
		self.cofs=coefficients
	def __repr__(self):
		"""More of a placeholder for a more complicated polynomial "render"."""
		return(str(self.cofs))
	def deriv(self):
		"""Takes the derivative of the polynomial and outputs a new polynomial"""
		newPoly=[]
		for i in range(len(self.cofs)-1,0,-1):
			newPoly.append(self.cofs[::-1][i]*i)
		return(Poly(newPoly))
	def __add__(self,oth):
		"""Surprisingly complicated for addition."""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		if(type(oth)!=Poly):raise Exception
		newPoly=[]
		self_=self.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(self.cofs))
		oth_=oth.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(oth.cofs))
		for i in range(len(self_)):
			newPoly.append(self_[i]+oth_[i])
		return(Poly(newPoly[::-1]))
	def __radd__(self,oth):
		"""Turns the other opperand (oth) to Poly if not already.
		Makes sure self are the same length, makes them if not.
		And adds every term together."""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		if(type(oth)!=Poly):raise Exception
		newPoly=[]
		self_=self.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(self.cofs))
		oth_=oth.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(oth.cofs))
		for i in range(len(self_)):
			newPoly.append(self_[i]+oth_[i])
		return(Poly(newPoly[::-1]))
a=Poly([1,2,3,4])
b=Poly([1,2,3,4])
print(1+a+b)