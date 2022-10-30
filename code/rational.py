from utils import gcd
class Rational:
	def __init__(self,numerator,denominator=1):
		if(denominator==0): raise ZeroDivisionError("Unallowed. Please add catch in your code")
		self.num=int(numerator) # Floor your floats today!
		self.denom=int(denominator)
		gcd_=gcd(self.num,self.denom)
		self.num//=gcd_
		self.denom//=gcd_
	def simplify(self):
		gcd_=gcd(self.num,self.denom)
		self.num//=gcd_
		self.denom//=gcd_
	def __repr__(self):
		return(str(self.num)+"/"+str(self.denom))
	def __add__(self,oth):
		"""(a/b)+(c/d)=(a*d+c*b)/(b*d) check it out!"""
		if(oth is int):oth=Rational(oth)
		return(Rational(self.num*oth.denom+oth.num*self.denom,self.denom*oth.denom).simplify())
	def __radd__(self,oth):
		"""Radical dude!"""
		if(oth is int):oth=Rational(oth)
		return(Rational(self.num*oth.denom+oth.num*self.denom,self.denom*oth.denom).simplify())
	def __sub__(self,oth):
		"""Hello and welcome to subway, how may I help you?"""
		return(Rational(self.num*oth.denom-oth.num*self.denom,self.denom*oth.denom).simplify())
	def __rsub__(self,oth):
		"""So many operations."""
		if(oth is int):oth=Rational(oth)
		return(Rational(oth.num*self.denom-self.num*oth.denom,self.denom*oth.denom).simplify())
	def __mul__(self,oth):
		""" "A hard one" (a/b)*(c/d)=(a*c)/(b*d)"""
		if(oth is int):oth=Rational(oth)
		return(Rational(self.num*oth.num,self.denom*oth.denom).simplify())
	def __rmul__(self,oth):
		"""I quit"""
		if(oth is int):oth=Rational(oth)
		return(Rational(self.num*oth.num,self.denom*oth.denom).simplify())
	def __truediv__(self,oth):
		"""No I don't (a/b)/(c/d)=(a*d)/(b*c)"""
		if(oth is int):oth=Rational(oth)
		return(Rational(self.num*oth.denom,self.denom*oth.num).simplify())
	def __rtruediv__(self,oth):
		"""Are true div"""
		if(oth is int):oth=Rational(oth)
		return(Rational(self.denom*oth.num,self.num*oth.denom).simplify())
