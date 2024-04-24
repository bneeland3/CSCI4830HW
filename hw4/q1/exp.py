import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Load the data from all_weeks.csv
data = pd.read_csv('all_weeks.csv')  # Adjust the filename to match your CSV file

# Adjust for the ascertainment rate by increasing reported cases
data['Adjusted_New_Cases'] = data['New Cases']  # You might need to adjust this based on the ascertainment rate

# Ensure adjusted incidence data does not contain zero or negative values
data['Adjusted_New_Cases'] = np.maximum(data['Adjusted_New_Cases'], 1)  # Set minimum value to 1

weekly_new_cases = data['Adjusted_New_Cases'].tolist()  # Use adjusted new case counts

# Step 2: Calculate the weekly incidence data
x = np.arange(len(weekly_new_cases))

# Step 3: Identify the period of exponential growth
start_week = 0
end_week = 15  # Adjust this based on the data to capture the exponential growth phase
x_subset = x[start_week:end_week]
y_subset = weekly_new_cases[start_week:end_week]  # Actual number of adjusted weekly new cases

# Step 4: Fit a linear regression model to estimate the slope (m)
X = x_subset.reshape(-1, 1)  # Reshape X for linear regression
reg = LinearRegression().fit(X, np.log(y_subset))  # Fit model using logarithm of y_subset for exponential growth
slope = reg.coef_[0]

# Step 5: Estimate R0
gamma = 1 / 2  # duration of infection
mu = 1 / 100   # typical life expectancy
R0 = 1 + (slope / (gamma + mu))

# Step 6: Calculate Confidence Interval for the Slope Estimate
n = len(y_subset)
y_pred = reg.predict(X)
residuals = np.log(y_subset) - y_pred
mse = np.sum(residuals ** 2) / (n - 2)  # Mean squared error
se_slope = np.sqrt(mse / np.sum((X - np.mean(X)) ** 2))  # Standard error of the slope
t = 2.262  # t-value for 95% confidence interval with n-2 degrees of freedom
slope_lower_bound = slope - t * se_slope
slope_upper_bound = slope + t * se_slope

# Step 7: Calculate Confidence Interval for R0 Estimate
R0_lower_bound = 1 + (slope_lower_bound / (gamma + mu))
R0_upper_bound = 1 + (slope_upper_bound / (gamma + mu))

# Step 8: Plot the scatterplot of weekly new cases and overlay the exponential fit
plt.scatter(x_subset, y_subset, label='Weekly New Cases', color='blue')  # Plot actual number of cases
plt.plot(x_subset, np.exp(reg.predict(X)), 'r-', label='Exponential Fit')  # Plot exponential fit
plt.xlabel('Week')
plt.ylabel('Number of New Cases')
plt.title('Exponential Growth of Cases')
plt.legend()
plt.grid(True)
plt.savefig('exp.png')

# Print the values
print("Estimated R0:", R0)
print("95% Confidence Interval for R0:", (R0_lower_bound, R0_upper_bound))
