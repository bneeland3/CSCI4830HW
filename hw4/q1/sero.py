import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def estimate_R0_from_seroprevalence(seroprevalence):
    return 1 / (1 - seroprevalence)

def calculate_confidence_interval(estimate, seroprevalence, sample_size):
    z_score = norm.ppf(0.975)  # For 95% confidence interval
    seronegative = sample_size - seroprevalence * sample_size
    standard_error = estimate * np.sqrt((seronegative / (seroprevalence ** 3)) / sample_size)
    lower_bound = estimate - z_score * standard_error
    upper_bound = estimate + z_score * standard_error
    return (lower_bound, upper_bound)

# Given seroprevalence data
seroprevalence = 517 / 1000  # 0.517
sample_size = 1000

# Estimate R0
estimated_R0 = estimate_R0_from_seroprevalence(seroprevalence)

# Calculate confidence interval for R0
confidence_interval = calculate_confidence_interval(estimated_R0, seroprevalence, sample_size)

# Plot
plt.figure(figsize=(8, 6))
plt.bar(x="Estimated R0", height=estimated_R0, yerr=[[estimated_R0 - confidence_interval[0]], [confidence_interval[1] - estimated_R0]], capsize=10, color='skyblue')
plt.title("Estimated R0 with 95% Confidence Interval")
plt.ylabel("R0")
plt.ylim(0, 4)  # Adjust y-axis limit for better visualization
plt.xticks([])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.text(0, estimated_R0 + 0.1, f"{estimated_R0:.2f}", ha='center')  # Add text label for R0
plt.text(0, confidence_interval[1] + 0.1, f"{confidence_interval[1]:.2f}", ha='center')  # Add text label for upper bound
plt.text(0, confidence_interval[0] - 0.15, f"{confidence_interval[0]:.2f}", ha='center')  # Add text label for lower bound
plt.savefig('sero.png')
