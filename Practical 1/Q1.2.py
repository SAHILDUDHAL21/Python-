from matplotlib.pyplot import *
from numpy import *

x = linspace(-2*pi,2*pi,100)
y=cos(x)
g=sin(x)
plot(x, y)
plot(x, g)
show()