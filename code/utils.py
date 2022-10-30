# Extra utility functions. Will be used later
def max(a,b,*args): # Max function for any number of arguments!
	if(len(args)==0):
		if(a>=b):return(a)
		else:return(b)
	maxi=a
	for i in args:
		maxi=max(maxi,i)
	return(maxi)
def min(a,b,*args): # Minimum function for any number of arguments!
	if(len(args)==0):
		if(a<=b):return(a)
		else:return(b)
	mini=a
	for i in args:
		mini=min(mini,i)
	return(mini)
def gcd(a,b): # Greatest common divisor. For Rational class
	while(a!=b and a!=0 and b!=0): #Euclidean algorithm
		a,b=b,a
		b=b%a
	return(max(a,b))
def summate(func,lower,upper): #summate=lambda f,l,u:sum([f(i) for i in range(l,u+1)])
	s=0
	for i in range(lower,upper+1):
		s+=func(i)
	return(s)
def product(func,lower,upper): #product=lambda f,l,u:[x:=x*f(i) for i in range(l,u+1)][-1]
	p=0
	for i in range(lower,upper+1):
		p*=func(i)
	return(p)
def integrate(func,lower,upper,density=10**5): #integrate=lambda f,l,u,d=10**5:sum([f(i/d)/d for i in range(l,u*d)])
	s=0
	for i in range(lower,upper*density):
		s+=func(i/density)/density
	return(s)
