import numpy as np

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
        # Update equations for S, I, R, V
        dS_dt = -beta * S * I / N
        
        if VE == 0:
            # When VE is 0, LM behaves like regular SIR
            dI_dt = beta * S * I / N - gamma * I
            dV_dt = 0  # No change in vaccinated individuals
        elif VE == 1:
            # When VE is 1, no new infections and everyone is vaccinated
            dI_dt = 0  # No change in infected individuals
            dV_dt = 0  # No change in vaccinated individuals
        else:
            dI_dt = beta * S * I / N + beta * V * I * (1 - VE) / N - gamma * I
            dV_dt = -(beta * V * (1 - VE)) / N  # Adjusted vaccination rate
        
        # Update values using Euler method
        S += delta_t * dS_dt
        I += delta_t * dI_dt
        R += delta_t * gamma * I
        V += delta_t * dV_dt
        
        susceptibles.append(S)
        infected.append(I)
        recovered.append(R)
        vaccinated.append(V)
        time.append(t + delta_t)  # Use current time t for consistency
    
    total_infections = max(infected)
    
    return time, susceptibles, infected, recovered, vaccinated, total_infections


def forward_euler_solver_anm(R_0, N, VE):
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
        
        if VE == 0:
            # When VE is 0, ANM behaves like regular SIR
            dI_dt = beta * S * I / N - gamma * I
            dV_null_dt = 0  # No change in vaccinated individuals
            dR_dt = gamma * I
            dV_all_dt = 0  # No change in vaccinated individuals
        elif VE == 1:
            # When VE is 1, no new infections and everyone is vaccinated
            dI_dt = 0  # No change in infected individuals
            dV_null_dt = 0  # No change in vaccinated individuals
            dR_dt = 0  # No change in recovered individuals
            dV_all_dt = 0  # No change in vaccinated individuals
        else:
            dI_dt = beta * S * I / N + beta * V_null * I / N - gamma * I
            dV_null_dt = -beta * V_null * I / N
            dR_dt = gamma * I
            dV_all_dt = N * VE * (-beta * S * I / N)
        
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
    
    total_infections = max(infected)
    
    return time, susceptibles, infected, recovered, vaccinated_null, vaccinated_all, total_infections
