from utils import *
equation=lambda x:2*x-x**2+1
assert max(0,1,8072,41,-8,2,8072,-7,-8,23)==8072 # Easiest with min
assert min(0,1,8072,41,-8,2,8072,-7,-8,23)==-8 # Easiest with max
assert summate(equation,0,5)==-19 # EZ
assert product(equation,0,5)==-392 # This took some tweaking for a nice answer.
assert gcd(369,36)==9 # The best test!
assert abs(integrate(equation,0,5)+35/3)<=10**-4 # Too imprecise. Can't fix myself.
assert abs(sqrt(2)-(2**0.5))<=10**-12 # Also imprecise, but alot better.
assert abs(sqrt(5432109876)-(5432109876**0.5))<=10**-12 # Check the large ones to.