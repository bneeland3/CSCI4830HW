import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Step 1: Load the data from all_weeks.csv
data = pd.read_csv('all_weeks.csv')  # Adjust the filename to match your CSV file
weekly_new_cases = data['New Cases'].tolist()  # Update column name if necessary

# Step 2: Calculate the weekly incidence data
x = np.arange(len(weekly_new_cases))

# Step 3: Identify the period of exponential growth
# For simplicity, let's assume the first few weeks represent the exponential growth phase
# You might need to adjust this based on the data
start_week = 0
end_week = 5  # Adjust as needed

# Step 4: Fit an exponential curve to this period and estimate the slope
def exponential_func(x, a, b):
    return a * np.exp(b * x)

x_subset = x[start_week:end_week]
y_subset = weekly_new_cases[start_week:end_week]

popt, pcov = curve_fit(exponential_func, x_subset, y_subset)
slope = popt[1]

# Step 5: Estimate R0
gamma = 2  # duration of infection
mu = 100   # typical life expectancy
R0 = 1 + (slope / (gamma + mu))

# Step 6: Plot the exponential growth curve and show the estimate of R0
plt.plot(x, weekly_new_cases, 'o', label='Weekly New Cases')
plt.plot(x_subset, exponential_func(x_subset, *popt), 'r-', label='Exponential Fit')
plt.xlabel('Week')
plt.ylabel('Number of New Cases')
plt.title('Exponential Growth of Cases')
plt.legend()
plt.grid(True)
plt.savefig('exp.png')

# Print the values
print("Optimal Parameters (popt):", popt)
print("Covariance Matrix (pcov):", pcov)
print("Estimated R0:", R0)
