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

# Bootstrap to estimate confidence interval
n_bootstraps = 1000
bootstrap_R0 = np.zeros(n_bootstraps)
for i in range(n_bootstraps):
    # Generate bootstrap sample by resampling with replacement
    bootstrap_infected_population = np.random.choice(infected_population, size=total_population, replace=True)
    bootstrap_total_population = np.random.choice(total_population, size=total_population, replace=True)
    bootstrap_ieq = np.mean(bootstrap_infected_population) / np.mean(bootstrap_total_population)
    
    # Estimate R0 from bootstrap sample
    bootstrap_R0[i] = estimate_R0_from_equilibrium_prevalence(bootstrap_ieq, gamma_over_mu)


# Calculate 95% confidence interval
lower_bound = np.percentile(bootstrap_R0, 2.5)
upper_bound = np.percentile(bootstrap_R0, 97.5)
print("95% Confidence Interval for R0:", (lower_bound, upper_bound))

# Plot
plt.figure(figsize=(8, 6))
plt.bar(x="Estimated R0", height=estimated_R0_equilibrium, color='skyblue')
plt.errorbar(x="Estimated R0", y=estimated_R0_equilibrium, yerr=[[abs(estimated_R0_equilibrium - lower_bound)], [abs(upper_bound - estimated_R0_equilibrium)]], fmt='o', color='black', capsize=5)
plt.title("Estimated R0 from Equilibrium Prevalence")
plt.ylabel("R0")
plt.ylim(0, 4)  # Adjust y-axis limit for better visualization
plt.xticks([])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.text(0, estimated_R0_equilibrium + 0.1, f"{estimated_R0_equilibrium:.2f}", ha='center')  # Add text label for R0
plt.savefig('prev.png')

