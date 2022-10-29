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
		for i in range(1,len(self.cofs)):
			newPoly.append(self.cofs[i]*(len(self.cofs)-i))
		return(Poly(newPoly))
