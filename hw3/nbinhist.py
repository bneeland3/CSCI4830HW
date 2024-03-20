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
k = 1.0  # Choose the value of k to plot the histogram for
generations = 10
trials = 100000

probability_die_out, outbreak_sizes = estimate_probability_die_out(R0, k, generations, trials)

# Plot histogram of outbreak sizes for the chosen k value
plt.figure(figsize=(10, 6))
plt.hist(outbreak_sizes, bins=10, alpha=0.7)
plt.title(f"Histogram of Outbreak Sizes for k = {k}")
plt.xlabel("Outbreak Size")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig('1khist.png')
plt.show()
