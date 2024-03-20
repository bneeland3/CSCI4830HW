import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def forward_euler_contact(s, i , p, omega, gamma, C, delta_t):
    # Calculate the next-generation matrix M
    P = np.diag(p)
    S = np.diag(s)
    M = np.dot(np.dot(np.dot(P, S), C), np.linalg.inv(np.diag(omega)))
    
    # Calculate the derivatives
    ds = - np.dot(M, i)
    di = np.dot(M, i) - np.dot(np.diag(gamma), i)
    
    # Update the susceptible and infected populations
    s_next = s + (ds * delta_t)
    i_next = i + (di * delta_t)
    
    return s_next, i_next

# Initialize known values
s_vec = np.array([0.99, 0.99, 0.99, 0.99])
i_vec = np.array([0.01, 0.01, 0.01, 0.01])
p_vec = np.array([1, 2, 3, 4])
omega_vec = np.array([0.25, 0.25, 0.25, 0.25])
gamma_vec = np.array([3, 3, 3, 3])
c_mat = np.array([
    [9/20, 9/20, 9/20, 9/20],
    [9/20, 9/20, 9/20, 9/20],
    [9/20, 9/20, 9/20, 9/20],
    [9/20, 9/20, 9/20, 9/20]
])

dt = 0.001
total_time = 3
iterations = int(total_time / dt)

# Running simulation and calculating average relative susceptibility simultaneously
s_vals = s_vec
i_vals = i_vec
p_avg = []

for i in range(iterations - 1):
    s_vec, i_vec = forward_euler_contact(s_vec, i_vec, p_vec, omega_vec, gamma_vec, c_mat, dt)
    s_vals = np.vstack((s_vals, s_vec))
    i_vals = np.vstack((i_vals, i_vec))
    
    # Calculate average relative susceptibility at each time step
    p_avg_t = np.dot(p_vec, s_vec) / np.sum(s_vec)
    p_avg.append(p_avg_t)

# Plotting infected proportions for groups 1-4 over time
plt.figure()
num_lines = len(i_vals[0])
t_vals = np.linspace(0, total_time, iterations)
colors = sns.color_palette("Blues", n_colors=num_lines)

for ind in range(num_lines):
    i = i_vals[:, ind]
    plt.plot(t_vals, i, label=f"Group {ind + 1}", color=colors[ind])

plt.xlabel("Time")
plt.ylabel("Infected Proportion")
plt.title("Infected Proportions for Groups 1-4 over Time")
plt.legend()
plt.savefig('infected_proportions.png')  # Saving the plot
plt.show()

# Plotting susceptible proportions for each group over time
plt.figure()
for ind in range(num_lines):
    s = s_vals[:, ind]
    plt.plot(t_vals, s, label=f"Group {ind + 1}", color=colors[ind])

plt.xlabel("Time")
plt.ylabel("Susceptible Proportion")
plt.title("Susceptible Proportions for Groups 1-4 over Time")
plt.legend()
plt.savefig('proportions.png')  # Saving the plot
plt.show()

# Plotting average relative susceptibility over time (in black)
plt.figure()
plt.plot(t_vals[:-1], p_avg, color='black')
plt.xlabel("Time")
plt.ylabel("Average Relative Susceptibility")
plt.title("Average Relative Susceptibility over Time")
plt.savefig('relative.png')  # Saving the plot
plt.show()
