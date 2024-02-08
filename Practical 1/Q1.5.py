from matplotlib.pyplot import *
from numpy import *

x=linspace(-1,1,100)
y=x**2
g=x*x*x

plot(x,y)
plot(x,g)
show()