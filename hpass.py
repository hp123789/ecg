from __future__ import division
from pylab import plot, xlim, show, grid
from numpy import loadtxt

data = loadtxt("putty.txt", float)

x = data[:,0]
y = data[:,1]


def Average(lst):
    return sum(lst) / len(lst)

average = Average(y)
average = float((round(average, 2))*1.2)

y1 = y

for n, i in enumerate(y1):
    if i < average:
        y1[n] = 0

plot(x, y)
xlim(4,14)
grid(True)
print(average)
print(y1)
show()