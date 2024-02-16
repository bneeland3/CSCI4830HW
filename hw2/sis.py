import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def forward_euler_solver(beta, gamma, s_0, i_0, delta_t, t_final):
    '''
    forward euler calculations for SIS model 
    '''
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
        
    # print(infected)
    # print(analytical)
    
    # returns a list of lists
    return [suceptibles, infected, time, analytical]

def get_E_delta_t(beta, gamma, s_0, i_0, delta_t, t_final):
    '''
    Function calcualtes E(delta_t)
    params: foware euler params
    '''
    data = forward_euler_solver(beta, gamma, s_0, i_0, delta_t, t_final)
    euler_soln = np.array(data[1])
    analytical_soln = np.array(data[3])
    
    E_delta_t = t_final * (np.abs(euler_soln - analytical_soln))
    
    return E_delta_t