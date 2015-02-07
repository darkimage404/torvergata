#!/usr/bin/env python

import pstats, cProfile

import pi_approx

cProfile.run("pi_approx.approx_pi()","Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()