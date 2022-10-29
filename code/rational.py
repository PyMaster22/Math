from utils.py import gcd
class Rational:
    def __init__(self,numerator,denominator=1):
        if(denominator==0): raise ZeroDivisionError("Unallowed. Please add catch in your code")
        self.num=int(numerator) # Floor your floats today!
        self.denom=int(denominator)
    def simplify(self):
        gcd_=gcd(self.num,self.denom)
        self.num=self.num//gcd_
        self.denom=self.denom//gcd_
    def __repr__(self):
        return(str(self.num)+"/"+str(self.denom))
    def __add__(self,oth):
        """(a/b)+(c/d)=(a*d+c*b)/(b*d) check it out!"""
        return(Rational(self.num*oth.denom+oth.num*self.denom,self.denom*oth.denom).simplify())
    def __radd__(self,oth):
        """Radical dude!"""
        return(Rational(self.num*oth.denom+oth.num*self.denom,self.denom*oth.denom).simplify())
    def __sub__(self,oth):
        """Hello and welcome to subway, how may I help you?"""
        return(Rational(self.num*oth.denom-oth.num*self.denom,self.denom*oth.denom).simplify())
    def __rsub__(self,oth):
        """So many operations."""
        return(Rational(oth.num*self.denom-self.num*oth.denom,self.denom*oth.denom).simplify())