from polynomial import *
a=Poly([0,00,1,2,1,8])
b=Poly([2,-1,243])
assert a==Poly([1,2,1,8])
assert b==Poly([2,-1,243])
assert a+b==Poly([1,4,0,251])
assert b+a==a+b
assert a-b==Poly([1,0,2,-235])
assert a*b==Poly([2,3,243,501,235,1944])
assert a!=b
assert a==a
assert b==b