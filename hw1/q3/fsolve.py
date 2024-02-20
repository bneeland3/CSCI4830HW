import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

'''
r_infinity = 1-e^-R_0*r_infinity
fsolve to find intersection point, then graph on a scatter plot!
f(r_infinity) = r_infinity
g(r_infinnity) = 1-e^-R_0*r_infinity

R_0 range = {0.9, 1.0, 1.1, 1.2}
'''

def find_f(r_infinity, R_0):
    return r_infinity

def find_g(r_infinity, R_0):
    g = 1-np.exp(-R_0*r_infinity)
    return g

# def get_intersection_point(R_0, R_0_range):
#     return fsolve(lambda r: find_f(r, R_0) - find_g(r, R_0), 0.5)[0]