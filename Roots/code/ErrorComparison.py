from __future__ import division
import sys
import os
import matplotlib.pyplot as plt
import scipy
from scipy import special

mydir = os.path.expanduser("~/")
sys.path.append(mydir + "/GitHub/PeasantMath/Roots/code")
import functions as fxn


ks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
ks = [3]

for i, k in enumerate(ks):

    fig = plt.figure()
    ax = fig.add_subplot(2,2,1)

    x = 2.0
    xs = []
    rts = []
    WLs = []
    guesses = []

    for j in range(100):

        xs.append(x)
        y = x**(1.0/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        a = abs(y - a)/y
        WLs.append(a)
        b = fxn.Guess(x, k)
        b = abs(y - b)/y
        guesses.append(b)
        x += 1

    #plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(k))
    plt.scatter(xs, WLs, color='c', alpha=0.9, label='WHL rule')
    #plt.scatter(xs, guesses, color='grey', alpha=0.9, label='Random guesses \nfor the remainder')
    plt.scatter(xs, guesses, color='grey', alpha=0.9, label='Assuming the remainder\nis 1/2')
    #plt.yscale('log')
    #plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    plt.xlim(min(xs), max(xs))
    #plt.ylim(min(WLs), max(rts))

    plt.legend(bbox_to_anchor=(-0.04, 1.1, 2.59, .3), loc=10, ncol=2,
               mode="expand",prop={'size':16})

    #leg = plt.legend(loc=4,prop={'size':12})
    #leg.draw_frame(False)
    #plt.text(-50, 14, "How well does the WHL Rule approximate square roots?", fontsize=16)



    ax = fig.add_subplot(2,2,2)
    x = 2.0
    xs = []
    rts = []
    WLs = []
    guesses = []

    for j in range(100):

        xs.append(x)
        y = x**(1.0/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        a = abs(y - a)/y
        WLs.append(a)
        b = fxn.Guess(x, k)
        b = abs(y - b)/y
        guesses.append(b)
        x += 10

    #plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(k))
    plt.scatter(xs, WLs, color='c', alpha=0.9)
    plt.scatter(xs, guesses, color='grey', alpha=0.9)
    #plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    plt.xlim(min(xs)*0.5, max(xs)*1.5)
    #plt.ylim(min(WLs)*0.5, max(rts)*1.5)


    ax = fig.add_subplot(2,2,3)
    x = 2.0
    xs = []
    rts = []
    WLs = []
    guesses = []

    for j in range(30):

        xs.append(x)
        y = x**(1.0/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        a = abs(y - a)/y
        WLs.append(a)
        b = fxn.Guess(x, k)
        b = abs(y - b)/y
        guesses.append(b)
        x = x*1.5


    #plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(k))
    plt.scatter(xs, WLs, color='c', alpha=0.9)
    plt.scatter(xs, guesses, color='grey', alpha=0.9)
    #plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    plt.xlim(min(xs)*0.5, max(xs)*1.5)
    #plt.ylim(min(WLs)*0.5, max(rts)*1.5)


    ax = fig.add_subplot(2,2,4)
    x = 2.0
    xs = []
    rts = []
    WLs = []
    guesses = []

    for j in range(30):

        xs.append(x)
        y = x**(1.0/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        a = abs(y - a)/y
        WLs.append(a)
        b = fxn.Guess(x, k)
        b = abs(y - b)/y
        guesses.append(b)
        x = x*2

    #plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(k))
    plt.scatter(xs, WLs, color='c', alpha=0.9)
    plt.scatter(xs, guesses, color='grey', alpha=0.9)
    #plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    plt.xlim(min(xs)*0.5, max(xs)*1.5)
    #plt.ylim(min(WLs)*0.5, max(rts)*1.5)


    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.subplots_adjust(wspace=0.5, hspace=0.3)
    plt.savefig(mydir+'/GitHub/PeasantMath/Roots/figs/ErrorAnalysis/error_and_0.5remainder-Root_'+str(k)+'.png', dpi=600, bbox_inches = 'tight')#, pad_inches=0)
    print 'finished root',k
    #plt.show()
