import numpy as np
import matplotlib.pyplot as plt
#problem 4
def SIR_model(N,S0,I0,R0,gamma,times):
    S, I, R = S0, I0, R0
    dt = 1
    S_list, I_list, R_list = [S], [I], [R]
    for time in range(1,times+1):
        dS = ((-R0*S*I/N) * dt)
        dI = (((R0*S*I/N)-(gamma*I))*dt)
        dR = ((gamma*I)*dt)
        S += dS
        I += dI
        R += dR
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    return np.array(S_list), np.array(I_list), np.array(R_list)
N = 10 ** 6
stable_R0 = 0.9
unstable_R0 = 1.1
gamma = 0.5
I0 = 1
R0 = 1
times = 50
eps = 1/N
Stable_S, Stable_I, Stable_R = SIR_model(N,N-eps, I0, stable_R0, gamma, times)
Unstable_S, Unstable_I, Unstable_R = SIR_model(N, N-eps, I0, unstable_R0, gamma, times)
S0, I0, R0 = SIR_model(N,N-eps,I0,R0,gamma,times)
plt.figure(figsize = (10,6))
plt.plot(range(times+1),Stable_I, label = 'I stable equilibrium Sahana', linestyle = 'dotted')
plt.plot(range(times+1),I0, label = 'I when R0 = 1 Sahana', linestyle = 'solid')
plt.plot(range(times+1), Unstable_I, label = 'I unstable equilibrium Sahana', linestyle = 'dashed')
plt.xlabel("Time")
plt.ylabel("People")
plt.legend()
plt.title("SIR Model Stability Sahana")

plt.savefig('stability.png')