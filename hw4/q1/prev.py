import numpy as np
import matplotlib.pyplot as plt

def estimate_R0_from_equilibrium_prevalence(ieq, gamma_over_mu):
    return 1 / (1 - ieq) * (gamma_over_mu + 1)

# Given data
infected_population = 7
total_population = 1000
bison_lifespan = 100
infection_duration = 2

# Calculate equilibrium prevalence
ieq = infected_population / total_population

# Calculate gamma_over_mu
gamma_over_mu = 1 / (bison_lifespan - infection_duration)

# Estimate R0 from equilibrium prevalence
estimated_R0_equilibrium = estimate_R0_from_equilibrium_prevalence(ieq, gamma_over_mu)
print("Estimated R0 from equilibrium prevalence:", estimated_R0_equilibrium)

# Bootstrapping
n_bootstraps = 1000
bootstrap_R0 = np.zeros(n_bootstraps)
for i in range(n_bootstraps):
    # Generate bootstrap sample by resampling with replacement
    bootstrap_ieq = np.random.choice([ieq], size=total_population, replace=True)
    
    # Estimate R0 from bootstrap sample
    bootstrap_R0[i] = estimate_R0_from_equilibrium_prevalence(np.mean(bootstrap_ieq), gamma_over_mu)

# Calculate 95% confidence interval
lower_bound = np.percentile(bootstrap_R0, 2.5)
upper_bound = np.percentile(bootstrap_R0, 97.5)
print("95% Confidence Interval for R0:", (lower_bound, upper_bound))

# Plot
plt.figure(figsize=(8, 6))
plt.bar(x="Estimated R0", height=estimated_R0_equilibrium, color='skyblue')
plt.title("Estimated R0 from Equilibrium Prevalence")
plt.ylabel("R0")
plt.ylim(0, 4)  # Adjust y-axis limit for better visualization
plt.xticks([])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.text(0, estimated_R0_equilibrium + 0.1, f"{estimated_R0_equilibrium:.2f}", ha='center')  # Add text label for R0
plt.show()
