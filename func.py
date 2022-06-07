from numpy.polynomial import Polynomial
a,b,c,d = (18,5,10,-30)
x = Polynomial([d,c,b,a])
print(x.roots())