import sys
import matplotlib
import matplotlib.pyplot as plt

'''
SIR model simulation: Forward Euler Method
y_n+1 = y_n + delta_y = y_n + delta_t(f(t_n, y_n)
t_n+1 = t_n + delt_t
first calculate delta_y?
Using Euler's generalize:
1. update t (t_1 = t_0 + delta_t) <-- x for time 
2. update s (S_1 = S_0 + delta_t*f(-beta*S_0*I_0/N)) <-- y for suceptible?
3. update r????

Test cases: 
1. beta = 1, gamma = 0.5
2. beta = 1.5, gamma = 0.5
3. beta = 2, gamma = 0.5

'''

def forward_euler_solver(beta, gamma):
    S = 999
    t_final = 50
    t_initial = 0
    I = 1
    N = 1000
    R = N - S - I
    
    suceptibles = [S]
    infected = [I]
    recovered = [R]
    time = [t_initial]
    delta_t = 1
    
    for t in range(t_initial, t_final):
        S_n = S + delta_t*(-beta*S*I/N) # update S
        I_n = I + delta_t*((beta*S*I/N)-(gamma*I)) # updatte I
        R_n = R + delta_t*(gamma*I) # update R
        suceptibles.append(S_n)
        infected.append(I_n)
        recovered.append(R_n)
        time.append(time[-1] + delta_t)
        
        S, I, R = S_n, I_n, R_n
        
    return [suceptibles, infected, recovered, time]

# print(forward_euler_solver(1.5, 0.5))

    