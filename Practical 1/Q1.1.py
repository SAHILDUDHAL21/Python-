#write a python program to plot 2D graph of the following function
# f(x)=x^2    [-2,2]

from matplotlib.pyplot import *
from numpy import *
x=linspace(-2,2)
y=x**2
plot(x,y)
show()
