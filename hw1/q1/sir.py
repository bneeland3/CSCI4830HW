import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
<<<<<<< HEAD
# from scipy.optimize import fsolve
=======
from scipy.optimize import fsolve
>>>>>>> a0de46fc7631987a853c9a2cb5d0e66429b41c1e

'''
SIR model simulation: Forward Euler Method
y_n = y_n-1 + delta_t*f(t_n,y_n)
t_n = t_n-1 + delta_ts

'''

def forward_euler_solver(beta, gamma, N):
    # below sets initial parameters
    S = 999
    t_final = 50
    t_initial = 0
    I = 1
    R = N - S - I
    
    # adds initial parameters to lists
    suceptibles = [S]
    infected = [I]
    recovered = [R]
    time = [t_initial]
    delta_t = 1
    
    for t in range(t_initial, t_final): # iterates through 0-50
        S_n = S + delta_t*(-beta*S*I/N) # update S
        I_n = I + delta_t*((beta*S*I/N)-(gamma*I)) # update I
        R_n = R + delta_t*(gamma*I) # update R
        # appends to lists
        suceptibles.append(S_n)
        infected.append(I_n)
        recovered.append(R_n)
        # updates time
        time.append(time[-1] + delta_t)
        
        # updates current SIR values to the new step
        S, I, R = S_n, I_n, R_n
        
    # returns a list of lists
    return [suceptibles, infected, recovered, time]

# print(forward_euler_solver(1.5, 0.5))
