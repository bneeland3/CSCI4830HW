import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

'''
SIR model simulation: Forward Euler Method
y_n = y_n-1 + delta_t*f(t_n,y_n)
t_n = t_n-1 + delta_ts

'''

def forward_euler_solver(S_0, I_0, R_0, gamma, N,):
    # below sets initial parameters
    t_initial = 0
    t_final = 50
    
    # adds initial parameters to lists
    suceptibles = [S_0]
    infected = [I_0]
    recovered = [R_0]
    time = [t_initial]
    
    epsilon = 1/N
    delta_t = 1
    
    for t in range(t_initial, t_final): # iterates through 0-50
        S_0 = N - epsilon
        dS = ((-R_0*S_0*I_0/N) * delta_t) # update S
        dI = (((R_0*S_0*I_0/N)-(gamma*I_0)) * delta_t) # update I
        dR = (gamma*I_0)* delta_t # update R
        
        # appends to lists
        S_0 = dS
        I_0 = dI
        R_0 = dR
        
        # S, I, R = S_n, I_n, R_n
        
        suceptibles.append(S_0)
        infected.append(I_0)
        recovered.append(R_0)
        # updates time
        time.append(time[-1] + delta_t)
        
        # updates current SIR values to the new step
    # solves for the intersection point for question 3
    print([suceptibles, infected, recovered, time])
    # returns a list of lists
    return [suceptibles, infected, recovered, time]

# print(forward_euler_solver(1.5, 0.5))
