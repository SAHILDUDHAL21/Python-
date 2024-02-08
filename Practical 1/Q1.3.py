from matplotlib.pyplot import *
from numpy import *

x = linspace(1,2*pi,100)
y=sin(x)-e**x+3*x-log(x)

plot(x,y)
show()