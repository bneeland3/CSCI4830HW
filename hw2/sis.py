import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from scipy.optimize import fsolve

'''
Normalized SIS Forward Euler Solver
S = -beta*s*i/N + gamma*i
I = beta*s*i/N - gamma*i
S + I = n
i_n = (beta - gamma)*i*(1-(i/(1-(1/R_0))))
s + i = 1
SIS with 3 plots t = 1, 0.5, 2
'''

def forward_euler_solver(beta, gamma, s_0, i_0, delta_t, t_final):
    # below sets initial parameters
    t = 0
    s = s_0
    i = i_0
    R_0 = (beta/gamma)
    
    # adds initial parameters to lists
    suceptibles = [s]
    infected = [i]
    time = [t]
    analytical = [i]
    
    ind = 1
    
    while t < t_final:
        ## logistic ODE
        i_t = (beta - gamma)*infected[ind-1]*(1-(infected[ind-1]/(1-(1/R_0))))
        
        ## closed form soln -- analytical
        exponential_term = np.exp(-(beta - gamma) * t)
        analytical_soln = ((1 - (1 / R_0)) / (1 + ((1 - (1 / R_0)) - i_0) / i_0 * exponential_term))

        # if R_0 != 0:  # Check to avoid division by zero
        #     exponential_term = np.exp(-(beta - gamma) * t)
        #     analytical_soln = (1 - (1 / R_0)) / (1 + (1 - (1 / R_0) - i_0) / (R_0 - i_0)) * i_0 * exponential_term
        # else:
        #     analytical_soln = 1  # Handle division by zero by setting analytical solution to 1

        # appends to lists
        i_next = (i_t * delta_t) + infected[ind-1]
        a_next = (analytical_soln * delta_t) + analytical[ind-1]
        
        infected.append(i_next)
        analytical.append(analytical_soln)
        
        # updates time
        t += delta_t
        time.append(t)
        
        # updates current SIS values to the new step
        i =  i_t
        
        # updates index
        ind += 1
        
    print(infected)
    print(analytical)
    
    # returns a list of lists
    return [suceptibles, infected, time, analytical]
