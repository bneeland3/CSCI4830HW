import numpy as np

def forward_euler_solver_lm(R_0, N, vaccine_efficiency):
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
    t_final = 300  # Increase simulation duration
    t_initial = 0
    delta_t = 0.01  # Decrease time step
    
    # Lists to store results
    susceptibles = [S]
    infected = [I]
    recovered = [R]
    vaccinated = [V]
    time = [t_initial]
    
    # Forward Euler method
    for t in np.arange(t_initial, t_final, delta_t):
        # Update equations for S, I, R
        S_n = S + delta_t * (-beta * S * I / N)
        I_n = I + delta_t * (beta * S * I / N - gamma * I)
        R_n = R + delta_t * (gamma * I)
        
        # Update equation for V (vaccinated individuals)
        V_n = V + delta_t * (vaccine_efficiency * (1 - V))
        
        susceptibles.append(S_n)
        infected.append(I_n)
        recovered.append(R_n)
        vaccinated.append(V_n)
        time.append(t + delta_t)  # Use current time t for consistency
        
        # Update values for next iteration
        S, I, R, V = S_n, I_n, R_n, V_n
        
    return time, susceptibles, infected, recovered, vaccinated


def forward_euler_solver_anm(R_0, N, vaccine_coverage):
    # Fixed duration for infectious period
    infectious_period = 14  # Assume a fixed duration for simplicity
    
    # Calculate beta from R_0
    beta = R_0 / infectious_period
    gamma = 1 / infectious_period
    
    # Initial conditions
    I = 1
    R = 0
    V_null = 0
    V_all = N * 0.5
    S = N - I - V_all
    
    # Time parameters
    t_final = 300  # Increase simulation duration
    t_initial = 0
    delta_t = 0.01  # Decrease time step
    
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
        dI_dt = beta * S * I / N - gamma * I
        dR_dt = gamma * I
        dV_null_dt = -beta * V_null * I
        dV_all_dt = N * vaccine_coverage * (-beta * S * I / N)
        
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
        time.append(t + delta_t)  # Use current time t for consistency
        
    return time, susceptibles, infected, recovered, vaccinated_null, vaccinated_all


