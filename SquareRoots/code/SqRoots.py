from __future__ import division
import sys
import os
import matplotlib.pyplot as plt
import scipy
from scipy import special
import numpy as np

mydir = os.path.expanduser("~/")


def root_of_closest_perfect_square(n):
    """ http://stackoverflow.com/questions/15390807/integer-square-root-in-python """
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def closest_perfect_kth_root(x, k): # x is the number of interest, k is the power

    y = 2
    while y <= x:
        y = y**k
        if y > x:
            return y**(1/k) - 1
        if y == x:
            y**(1/k)

        y = y**(1/k)
        y += 1




def WHL_kth(x, k):

    n = closest_perfect_kth_root(x, k) # x is the number of interest, k is the power
    i = 1
    a = 0
    while i <= k:
        b = scipy.special.binom(k, 1)
        a += (b*(n**(k-i)))
        i += 1

    a = (x - n**k)/a
    a += n

    return float(a)




fig = plt.figure()
ax = fig.add_subplot(2,2,1)

x = 2
k = 5
xs = []
rts = []
WLs = []

for i in range(100):

    xs.append(x)
    y = x**(1/k)
    rts.append(y)
    a = WHL_kth(x, k)
    WLs.append(a)
    x += 1

plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
plt.scatter(xs, WLs, color='c', alpha=0.9, label='WBL rule')
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=4,prop={'size':12})
leg.draw_frame(False)
#plt.text(-50, 14, "How well does the Webster-Locey Rule approximate square roots?", fontsize=16)




ax = fig.add_subplot(2,2,2)
x = 2
xs = []
sqrts = []
WLs = []

for i in range(100):

    xs.append(x)
    y = x**(1/k)
    sqrts.append(y)
    a = WHL_kth(x, k)
    WLs.append(a)

    x += 10


plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
plt.scatter(xs, WLs, color='c', alpha=0.9, label='WBL rule')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':12})
leg.draw_frame(False)




ax = fig.add_subplot(2,2,3)
x = 2.0
xs = []
sqrts = []
WLs = []

for i in range(30):

    xs.append(x)
    y = x**(1/k)
    sqrts.append(y)
    a = WHL_kth(x, k)
    WLs.append(a)

    x = x*1.5


plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
plt.scatter(xs, WLs, color='c', alpha=0.9, label='WBL rule')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=4,prop={'size':12})
leg.draw_frame(False)


ax = fig.add_subplot(2,2,4)
x = 2.0
xs = []
sqrts = []
WLs = []

for i in range(30):

    xs.append(x)
    y = x**(1/k)
    sqrts.append(y)
    a = WHL_kth(x, k)
    WLs.append(a)

    x = x*2

plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
plt.scatter(xs, WLs, color='c', alpha=0.9, label='WBL rule')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':13})
leg.draw_frame(False)

plt.tick_params(axis='both', which='major', labelsize=8)
plt.subplots_adjust(wspace=0.5, hspace=0.3)
plt.savefig(mydir+'/GitHub/PeasantMath/SquareRoots/figs/WHL_root'+str(int(k))+'.png', dpi=600)#, bbox_inches = 'tight')#, pad_inches=0)
#plt.show()
