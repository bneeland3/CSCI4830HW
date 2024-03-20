import numpy as np
import matplotlib.pyplot as plt

def simulate_branching_process(R0, k, generations):
    infected = np.array([1])
    outbreak_sizes = []

    mean = R0
    variance = mean + (mean**2)/k
    p = mean / variance
    n = mean**2 / (variance - mean)

    for _ in range(generations):
        secondary_infections = np.random.negative_binomial(n, p, size=len(infected))
        infected = np.concatenate((infected, secondary_infections))
        if np.sum(secondary_infections) == 0:
            outbreak_sizes.append(len(infected))
            break
        outbreak_sizes.append(len(infected))

    return outbreak_sizes

def estimate_probability_die_out(R0, k, generations, trials):
    die_out_count = 0
    outbreak_sizes = []

    for _ in range(trials):
        outbreak_size = simulate_branching_process(R0, k, generations)
        if len(outbreak_size) == generations + 1:
            die_out_count += 1
        else:
            outbreak_sizes.extend(outbreak_size)

    probability_die_out = die_out_count / trials
    return probability_die_out, outbreak_sizes

R0 = 3
k_values = [0.1, 0.5, 1.0, 5.0, 10.0]
generations = 25
trials = 100000

outbreak_size_data = {}

for k in k_values:
    probability_die_out, outbreak_sizes = estimate_probability_die_out(R0, k, generations, trials)
    outbreak_size_data[k] = outbreak_sizes

    print(f"For k = {k}:")
    print(f"Probability of epidemic dying out in finite time: {probability_die_out:.3f}")

# Plot histogram of outbreak sizes
plt.figure(figsize=(10, 6))
plt.hist(outbreak_size_data.values(), bins=20, label=[f"k = {k}" for k in k_values], alpha=0.7)
plt.title("Histogram of Outbreak Sizes")
plt.xlabel("Outbreak Size")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.savefig('allks.png')
plt.show()
