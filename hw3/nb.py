import numpy as np
from scipy.stats import nbinom

def simulate_branching_process(R0, k, generations):
    '''
    Params
    ------
    
    Returns
    -------
    '''
    # branching array functions!! add params and description please.
    infected = np.array([1])

    for _ in range(generations):
        mean = R0
        variance = mean + (mean**2)/k
        p = mean / variance
        n = mean**2 / (variance - mean)
        secondary_infections = nbinom.rvs(n=n, p=p, size=len(infected))
        infected = np.concatenate((infected, secondary_infections))
        if np.sum(secondary_infections) == 0:
            return True
    return False

def estimate_probability_die_out(R0, k, generations, trials):
    die_out_count = sum(simulate_branching_process(R0, k, generations) for _ in range(trials))
    return die_out_count / trials

R0_values = [3]
k_values = [0.1, 0.5, 1.0, 5.0, 10.0]
generations = 25
trials = 100000  # Adjust this value to reduce the number of trials

results = {}

for R0 in R0_values:
    for k in k_values:
        probability_die_out = estimate_probability_die_out(R0, k, generations, trials)
        results[(R0, k)] = probability_die_out

# Write results to a file
with open("epidemic_probability_table.txt", "w") as file:
    file.write("Probability of epidemic dying out in finite time:\n")
    file.write("R0\tk\tProbability (q)\n")
    for R0, k in sorted(results.keys()):
        file.write(f"{R0}\t{k}\t{results[(R0, k)]:.3f}\n")

print("Table has been written to 'epidemic_probability_table.txt'.")
