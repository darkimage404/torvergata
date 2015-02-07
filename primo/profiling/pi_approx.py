#!/usr/bin/env python

def recip_square(i):
    return 1./i**2

def approx_pi(n=10000000):
    """ Function which gives an approximation of pi. The relation we use has been proven by Euler in 1735
        and is known as the Basel problem. """
    val = 0.
    for k in range(1,n+1):
        val += recip_square(k)
    return (6 * val)**.5
