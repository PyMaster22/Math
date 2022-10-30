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
	def __int__(self):
		return(self.num//self.denom)
	def __add__(self,oth):
		"""(a/b)+(c/d)=(a*d+c*b)/(b*d) check it out!"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.num*oth.denom+oth.num*self.denom,self.denom*oth.denom))
	def __radd__(self,oth):
		"""Radical dude!"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.num*oth.denom+oth.num*self.denom,self.denom*oth.denom))
	def __sub__(self,oth):
		"""Hello and welcome to subway, how may I help you?"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.num*oth.denom-oth.num*self.denom,self.denom*oth.denom))
	def __rsub__(self,oth):
		"""So many operations."""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(oth.num*self.denom-self.num*oth.denom,self.denom*oth.denom))
	def __mul__(self,oth):
		""" "A hard one" (a/b)*(c/d)=(a*c)/(b*d)"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.num*oth.num,self.denom*oth.denom))
	def __rmul__(self,oth):
		"""I quit"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.num*oth.num,self.denom*oth.denom))
	def __truediv__(self,oth):
		"""No I don't (a/b)/(c/d)=(a*d)/(b*c)"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.num*oth.denom,self.denom*oth.num))
	def __rtruediv__(self,oth):
		"""Are true div"""
		if(type(oth)==int):oth=Rational(oth)
		return(Rational(self.denom*oth.num,self.num*oth.denom))
	def __mod__(self,oth):
		"""Modulus with more basic operations."""
		if(type(oth)==int):oth=Rational(oth)
		return(oth*((self/oth)-int(self/oth)))
	def __rmod__(self,oth):
		if(type(oth)==int):oth=Rational(oth)
		return(oth*((self/oth)-int(self/oth)))
	def __pow__(self,oth):
		"""Reverse is just non integer powers."""
		if(type(oth)!=int):raise Exception("I'm not gonna do this!")
		return(Rational(self.num**oth,self.denom**oth))
a=Rational(3,4)
print(a**3)