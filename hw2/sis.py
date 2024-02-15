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
    
    ind = 1
    
    while t < t_final:
        ## logistic ODE
        i_t = (beta - gamma)*infected[ind-1]*(1-(infected[ind-1]/(1-(1/R_0))))
        ## closed form soln
        # if np.isclose(i, 1):  # Check if i is close to 1 to avoid division by zero
        #     i_t = 1
        # else:
        #     exponential_term = np.exp(-(beta - gamma) * t)
        #     fraction_term = ((1 - (1 / R_0)) / (1 + (1 - (1 / R_0) - i_0) / (R_0 * i_0)))
        #     i_t = 1 - fraction_term * i_0 * exponential_term

        # appends to lists
        i_next = (i_t * delta_t) + infected[ind-1]
        infected.append(i_next)
        
        # updates time
        t += delta_t
        time.append(t)
        
        # updates current SIS values to the new step
        i =  i_t
        
        ind += 1
        

    print(infected)
    # returns a list of lists
    return [suceptibles, infected, time]
