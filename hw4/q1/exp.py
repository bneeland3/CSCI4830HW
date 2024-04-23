import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Load the data from all_weeks.csv
data = pd.read_csv('all_weeks.csv')  # Adjust the filename to match your CSV file

# Adjust for the ascertainment rate by increasing reported cases
data['Adjusted_New_Cases'] = data['New Cases'] * 10  # Multiply by 10 for the ascertainment rate

# Ensure adjusted incidence data does not contain zero or negative values
data['Adjusted_New_Cases'] = np.maximum(data['Adjusted_New_Cases'], 1)  # Set minimum value to 1

weekly_new_cases = data['Adjusted_New_Cases'].tolist()  # Use adjusted new case counts

# Step 2: Calculate the weekly incidence data
x = np.arange(len(weekly_new_cases))

# Step 3: Identify the period of exponential growth
# For simplicity, let's assume the first few weeks represent the exponential growth phase
# You might need to adjust this based on the data
start_week = 0
end_week = 15 # len(weekly_new_cases)  # Use all weeks from the dataset

# Subset the data for the exponential growth phase
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

# Step 6: Plot the scatterplot of weekly new cases and overlay the exponential fit
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
