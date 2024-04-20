import numpy as np
import matplotlib.pyplot as plt

def forward_euler_solver_lm(R_0, N, VE):
    # Fixed duration for infectious period
    infectious_period = 14  # Assume a fixed duration for simplicity
    
    # Calculate recovery rate gamma from infectious period
    gamma = 1 / infectious_period
    
    # Calculate beta from R_0
    beta = R_0 / infectious_period
    
    # Initial conditions
    I = 1
    S = N - I
    R = 0
    V = 0
    
    # Time parameters
    t_final = 300
    t_initial = 0
    delta_t = 0.01
    
    # Lists to store results
    susceptibles = [S]
    infected = [I]
    recovered = [R]
    vaccinated = [V]
    time = [t_initial]
    
    # Forward Euler method
    for t in np.arange(t_initial, t_final, delta_t):
        # Update equations for S, I, R, V
        dS_dt = -beta * S * I / N
        
        if VE == 0:
            dI_dt = beta * S * I / N - gamma * I
            dV_dt = 0
        elif VE == 1:
            dI_dt = 0
            dV_dt = 0
        else:
            dI_dt = beta * S * I / N + beta * V * I * (1 - VE) / N - gamma * I
            dV_dt = -(beta * V * (1 - VE)) / N
        
        S += delta_t * dS_dt
        I += delta_t * dI_dt
        R += delta_t * gamma * I
        V += delta_t * dV_dt
        
        susceptibles.append(S)
        infected.append(I)
        recovered.append(R)
        vaccinated.append(V)
        time.append(t + delta_t)
    
    total_infections = max(infected)
    
    return time, susceptibles, infected, recovered, vaccinated, total_infections


def forward_euler_solver_anm(R_0, N, VE):
    # Fixed duration for infectious period
    infectious_period = 14
    
    # Calculate beta from R_0
    beta = R_0 / infectious_period
    gamma = 1 / infectious_period
    
    # Initial conditions
    I = 1
    R = 0
    V_null = 0
    V_all = N * VE
    S = N - I - V_all
    
    # Time parameters
    t_final = 300
    t_initial = 0
    delta_t = 0.01
    
    # Lists to store results
    susceptibles = [S]
    infected = [I]
    recovered = [R]
    vaccinated_null = [V_null]
    vaccinated_all = [V_all]
    time = [t_initial]
    
    # Forward Euler method
    for t in np.arange(t_initial, t_final, delta_t):
        # Update equations for S, I, R, V_null, and V_all
        dS_dt = -beta * S * I / N
        
        if VE == 0:
            dI_dt = beta * S * I / N - gamma * I
            dV_null_dt = 0
            dR_dt = gamma * I
            dV_all_dt = 0
        elif VE == 1:
            dI_dt = 0
            dV_null_dt = 0
            dR_dt = 0
            dV_all_dt = 0
        else:
            dI_dt = beta * S * I / N + beta * V_null * I / N - gamma * I
            dV_null_dt = -beta * V_null * I / N
            dR_dt = gamma * I
            dV_all_dt = -(beta * V_all) / N
        
        S += delta_t * dS_dt
        I += delta_t * dI_dt
        R += delta_t * dR_dt
        V_null += delta_t * dV_null_dt
        V_all += delta_t * dV_all_dt
        
        susceptibles.append(S)
        infected.append(I)
        recovered.append(R)
        vaccinated_null.append(V_null)
        vaccinated_all.append(V_all)
        time.append(t + delta_t)
    
    total_infections = max(infected)
    
    return time, susceptibles, infected, recovered, vaccinated_null, vaccinated_all, total_infections

# Parameters
N = 300000
VE_values = [0.8]
R0_vals = [3, 4, 5]

# Plotting
for VE in VE_values:
    for R0 in R0_vals:
        # Leaky Model (LM)
        time_lm, S_lm, I_lm, R_lm, V_lm, total_infections_lm = forward_euler_solver_lm(R0, N, VE)
        label_lm = f"LM, VE = {VE}, R0 = {R0}"
        
        # All-or-Nothing Model (ANM)
        time_anm, S_anm, I_anm, R_anm, V_null_anm, V_all_anm, total_infections_anm = forward_euler_solver_anm(R0, N, VE)
        label_anm = f"ANM, VE = {VE}, R0 = {R0}"
        
        # Plot infected individuals over time
        plt.figure(figsize=(12, 6))
        plt.plot(time_lm, [(i / N) * 100 for i in I_lm], label=label_lm)
        plt.plot(time_anm, [(i / N) * 100 for i in I_anm], label=label_anm)
        plt.title(f"Infected Individuals over Time - VE = {VE}, R0 = {R0}")
        plt.xlabel("Time (days)")
        plt.ylabel("Percentage of Infected Individuals")
        plt.legend()
        plt.show()
        
        # Print total infections
        print(f"Total Infections - {label_lm}: {total_infections_lm}")
        print(f"Total Infections - {label_anm}: {total_infections_anm}")