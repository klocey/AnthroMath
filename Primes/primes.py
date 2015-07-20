from __future__ import division
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import special

import sys

mydir = os.path.expanduser("~/")
sys.path.append(mydir + "/GitHub/PeasantMath/Roots/code")
import functions as fxn


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
nums = range(2, max(primes)+ 1)

passes = 0
fails = 0

for i, num in enumerate(nums):

    # RULE HIERARCHY
    # 1.) IS DIVISIBLE BY 2? IF YES, THEN NUM IS NOT PRIME
    r = num%2
    if r == 0 and r != 2:
        print num,'is not prime:',
        if num in primes:
            print 'fail'
            fails += 1
        else:
            print 'pass'
            passes += 1
        continue

    # GET CLOSEST (FLOOR) PERFECT SQUARE
    k = 2
    pf = fxn.closest_perfect_kth_root(num, k) # x is the number of interest, k is the power

    if num == pf**2 - 1:
        print num, 'is not prime:',
        if num in primes:
            print 'fail'
            fails += 1
        else:
            print 'pass'
            passes += 1
        continue


    # CHECK FOR A PERFECT SQUARE
    if pf == num:
        print num,'is not prime:',
        if num in primes:
            print 'fail'
            fails += 1
        else:
            print 'pass'
            passes += 1
        continue

    # GET THE REMAINDER
    rem = num - pf

    # FIND THE SIZE OF THE LEGS LEXICALLY
    #if rem > np.sqrt(pf):
    #    x1 = np.sqrt(pf)
    #    x2 = rem - x1
    #elif rem <= np.sqrt(pf):
    #    x1 = rem
    #    x2 = 0

    # DIVIDE THE REMAINDER INTO TWO NATURAL NUMBERS OF CLOSEST VALUE
    x1 = rem/2.0 + 0.5
    x2 = rem/2.0 - 0.5

    # APPLY SOME More RULES
    # 1.) If one leg is 0.0, is the other leg 1 or prime, if so, then num should be prime
    if x2 == 0:
        if x1 < np.sqrt(num):
            if x1 in primes or x1 == 1:
                print num,'should be prime:',
                if num in primes:
                    print 'pass'
                    passes += 1

                else:
                    print num,'fail'
                    fails += 1

    # 2.) IS THE SUM OF THE PRIME LEGS A PRIME? IF SO, THE NUM SHOULD NOT BE PRIME
    if x1 in primes and x2 in primes:
        x3 = x1 + x2
        if x3 in primes:
            print num,'should not be prime:',
            if num in primes:
                print 'fail'
                fails += 1
            else:
                print'pass'
                passes += 1

    # 3.) IS
    elif x1 in primes or x2 in primes:
        print num,'should be prime',
        if num in primes:
            print 'pass'
            fails += 1
        else:
            print 'fail'
            passes += 1
        continue

    elif x1 == 1 or x2 == 1:
        print num,'should be prime',
        if num in primes:
            print 'pass'
            fails += 1
        else:
            print 'fail'
            passes += 1
        continue

print passes, fails, passes/(fails + passes)
