# Extra utility functions. Will be used later
def max(a,b,*args): # Max function for any number of arguments!
    if(len(args)==0):
        if(a>=b):return(a)
        else:return(b)
    maxi=a
    for i in args:
        maxi=max(maxi,i)
    return(maxi)
def gcd(a,b): # Greatest common divisor. For Rational class
    while(a!=b and a!=0 and b!=0): #Euclidean algorithm
        a,b=b,a
        b=b%a
    return(max(a,b))
