from rational import Rational
from utils import max
class Poly:
	"""A polynomial class."""
	def __init__(self,coeffs):
		newcofs=[]
		foundNotZero=False
		for i in coeffs:
			if(i==0 and not foundNotZero):continue
			else:foundNotZero=True
			newcofs.append(i)
		self.cofs=newcofs
	def __repr__(self):
		"""More of a placeholder for a more complicated polynomial "render"."""
		return(str(self.cofs))
	def __str__(self):
		return(self.__repr__())
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
	def __sub__(self,oth):
		"""Subtraction for the loss!"""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		if(type(oth)!=Poly):raise Exception
		newPoly=[]
		self_=self.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(self.cofs))
		oth_=oth.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(oth.cofs))
		for i in range(len(self_)):
			newPoly.append(self_[i]-oth_[i])
		return(Poly(newPoly[::-1]))
	def __rsub__(self,oth):
		"""It's the same as addition, just minus. And order matters here."""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		if(type(oth)!=Poly):raise Exception
		newPoly=[]
		self_=self.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(self.cofs))
		oth_=oth.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(oth.cofs))
		for i in range(len(self_)):
			newPoly.append(oth_[i]-self_[i])
		return(Poly(newPoly[::-1]))
	def __mul__(self,oth):
		"""Multiplication. O(n^2)"""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		if(type(oth)!=Poly):raise Exception
		newPoly={}
		for j,i in enumerate(self.cofs[::-1]):
			for jj,ii in enumerate(oth.cofs[::-1]):
				try:
					newPoly[j+jj]+=i*ii
				except KeyError:
					newPoly[j+jj]=i*ii
		return(Poly(list(newPoly.values())[::-1]))
	def __rmul__(self,oth):
		"""Found another implementation for this entire idea while looking for help on the previous operation :>"""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		if(type(oth)!=Poly):raise Exception
		newPoly={}
		for j,i in enumerate(self.cofs[::-1]):
			for jj,ii in enumerate(oth.cofs[::-1]):
				try:
					newPoly[j+jj]+=i*ii
				except KeyError:
					newPoly[j+jj]=i*ii
		return(Poly(list(newPoly.values())[::-1]))
	def __eq__(self,oth):
		"""Can't think of an easier way."""
		if(type(oth)in[int,Rational]):oth=Poly([oth])
		self_=self.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(self.cofs))
		oth_=oth.cofs[::-1]+[0]*(max(len(self.cofs),len(oth.cofs))-len(oth.cofs))
		for i in range(len(self_)):
			if(self_[i]!=oth_[i]):return(False)
		return(True)