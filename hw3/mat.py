import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def forward_euler_contact(s, i , p, omega, gamma, C, delta_t):
    
    M =np.dot(np.dot(np.dot(np.diag(s), np.diag(p)), C), np.linalg.inv(np.diag(omega)))
    
    ds = - np.dot(M, i)
    di = np.dot(M, i) - np.dot(np.diag(gamma), i)
    
    s_next = s + (ds*delta_t)
    i_next = i + (di*delta_t)
    
    return s_next, i_next

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

# running simulation
s_vals = s_vec
i_vals = i_vec
for i in range(iterations - 1):
    s_vec, i_vec = forward_euler_contact(s_vec, i_vec, p_vec, omega_vec, gamma_vec, c_mat, dt)
    s_vals = np.vstack((s_vals, s_vec))
    i_vals = np.vstack((i_vals, i_vec))
    

# Number of lines
num_lines = len(i_vals[0])
t_vals = np.linspace(0, total_time, iterations)

# Create a color palette with successive lighter hues of red
colors = sns.color_palette("Blues", n_colors=num_lines)

# Plotting
for ind in range(num_lines):
    i = i_vals[:, ind]
    plt.plot(t_vals, i, label=f"Group {ind + 1}", color=colors[ind])

# Set plot labels and title
plt.xlabel("Time")
plt.ylabel("Infected Proportion")
plt.title("Infected Proportions for Groups 1-4 over Time")

# Display legend
plt.legend()

# saves plot
plt.savefig('contact.png')

# Show the plot
plt.show()
