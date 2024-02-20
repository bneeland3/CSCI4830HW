import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from scipy.optimize import fsolve

'''
SIR model simulation: Forward Euler Method
y_n = y_n-1 + delta_t*f(t_n,y_n)
t_n = t_n-1 + delta_ts
'''
def forward_euler_solver(beta, gamma, N, R_0):
    # Initial conditions
    I = 1
    S = N - I
    R = 0
    
    # Time parameters
    t_final = 50
    t_initial = 0
    delta_t = 1
    
    # Lists to store results
    susceptibles = [S]
    infected = [I]
    recovered = [R]
    time = [t_initial]
    
    # Forward Euler method
    for t in range(t_initial, t_final):
        S_n = S + delta_t * (-beta * S * I / N)
        I_n = I + delta_t * ((beta * S * I / N) - (gamma * I))
        R_n = R + delta_t * (gamma * I)
        
        susceptibles.append(S_n)
        infected.append(I_n)
        recovered.append(R_n)
        time.append(time[-1] + delta_t)
        
        # Update values for next iteration
        S, I, R = S_n, I_n, R_n
        
    return time, susceptibles, infected, recovered