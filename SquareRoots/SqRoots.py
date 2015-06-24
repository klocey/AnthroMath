from __future__ import division
import sys
import os
import matplotlib.pyplot as plt

mydir = os.path.expanduser("~/")


def closest_perfect_square(n):
    """ http://stackoverflow.com/questions/15390807/integer-square-root-in-python """

    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


fig = plt.figure()
ax = fig.add_subplot(2,2,1)

x = 1
xs = []
sqrts = []
WLs = []

for i in range(100):

    xs.append(x)
    y = x**0.5
    sqrts.append(y)

    y1 = closest_perfect_square(x) # actually gives the square root of it
    y2 = y1 + 1
    z1 = x - y1**2
    z2 = float(y1 + y2)
    a = y + z1/z2
    WLs.append(a)
    x += 1

plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='square root')
plt.scatter(xs, WLs, color='c', alpha=0.9, label='W&L rule')
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':12})
leg.draw_frame(False)
plt.text(-50, 14, "How well does the Webster-Locey Rule approximate square roots?", fontsize=16)




ax = fig.add_subplot(2,2,2)
x = 2
xs = []
sqrts = []
WLs = []

for i in range(100):

    xs.append(x)
    y = x**0.5
    sqrts.append(y)

    y1 = closest_perfect_square(x) # actually gives the square root of it
    y2 = y1 + 1
    z1 = x - y1**2
    z2 = float(y1 + y2)
    a = y + z1/z2
    WLs.append(a)
    x += 10

plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='square root')
plt.scatter(xs, WLs, color='c', alpha=0.9, label='W&L rule')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':12})
leg.draw_frame(False)




ax = fig.add_subplot(2,2,3)
x = 2
xs = []
sqrts = []
WLs = []

for i in range(30):

    xs.append(x)
    y = x**0.5
    sqrts.append(y)

    y1 = closest_perfect_square(x) # actually gives the square root of it
    y2 = y1 + 1
    z1 = x - y1**2
    z2 = float(y1 + y2)
    a = y + z1/z2
    WLs.append(a)
    x = x*1.5

plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='square root')
plt.scatter(xs, WLs, color='c', alpha=0.9, label='W&L rule')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':12})
leg.draw_frame(False)



ax = fig.add_subplot(2,2,4)
x = 2
xs = []
sqrts = []
WLs = []

for i in range(30):

    xs.append(x)
    y = x**0.5
    sqrts.append(y)

    y1 = closest_perfect_square(x) # actually gives the square root of it
    y2 = y1 + 1
    z1 = x - y1**2
    z2 = float(y1 + y2)
    a = y + z1/z2
    WLs.append(a)
    x = x*2

plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='square root')
plt.scatter(xs, WLs, color='c', alpha=0.9, label='W&L rule')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':13})
leg.draw_frame(False)

plt.tick_params(axis='both', which='major', labelsize=8)
plt.subplots_adjust(wspace=0.5, hspace=0.3)
plt.savefig(mydir+'/GitHub/AnthroMath/SquareRoots/WebsterLoceyRule.png', dpi=600)#, bbox_inches = 'tight')#, pad_inches=0)
#plt.show()
