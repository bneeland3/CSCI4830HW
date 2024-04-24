import argparse
import numpy as np
import matplotlib.pyplot as plt
from assay import read_csvs, get_se, get_sp, get_theta_hat, get_phi_hat, get_youden_j_c

def main():
    # The argparse library allows us to take command-line arguments
    parser = argparse.ArgumentParser(
        description='Plot ELISA data',
        prog='ELISA Scatter Plot')

    parser.add_argument('--pos_data',
                        type=str,
                        help='CSV positive data file name',
                        required=True) 
    
    parser.add_argument('--neg_data',
                        type=str,
                        help='CSV negative data file name',
                        required=True) 
    
    parser.add_argument('--field_data',
                        type=str,
                        help='CSV field data file name',
                        required=True) 
        
    parser.add_argument('--cutoff',
                        type=float,
                        help='cutoff value for assay data',
                        required=False)  # cutoff parameter, change in bash script
    
    parser.add_argument('--output_file_assay',
                        type=str,
                        help='Output file name',
                        required=True)  
    
    parser.add_argument('--output_file_roc',
                        type=str,
                        help='Output file name',
                        required=False)  
    
    parser.add_argument('--output_file_theta',
                        type=str,
                        help='Output file name',
                        required=False)  
    
    args = parser.parse_args()
    
    # Read CSV files
    files = [args.pos_data, args.neg_data, args.field_data]
    data = read_csvs(files)
    
    if args.cutoff:
        specificity = get_sp(args.cutoff, data[0])
        sensitivity = get_se(args.cutoff, data[1])
        phi_hat = get_phi_hat(args.cutoff, data[2])  # Calculate phi_hat here
        j_c = get_youden_j_c(sensitivity, specificity)
        theta = get_theta_hat(sensitivity, specificity, phi_hat)
        print(f'Theta: {theta}')
        print(f'Youden J(c): {j_c}')
    
    if args.output_file_roc and args.output_file_theta: 
        # Determine the minimum and maximum cutoff values from the field data
        min_c = min(data[2])
        max_c = max(data[2])

        # Define a range of cutoff values between the minimum and maximum
        num_points = 50  # Adjust the number of points as needed for smoother curve
        c_values = np.linspace(min_c, max_c, num_points)
        
        # Normalize cutoff values to the range [0, 1]
        norm_c_values = (c_values - min_c) / (max_c - min_c)
        
        # Initialize lists to store sensitivity, specificity, corrected prevalence, and Youden index for each cutoff value
        sensitivity_values = []
        specificity_values = []
        theta_values = []
        youden_values = []  # Initialize the list for Youden values

        # Iterate over each cutoff value
        for c in c_values:
            # Calculate sensitivity, specificity, and corrected prevalence for the current cutoff value
            sensitivity = get_se(c, data[1])
            specificity = get_sp(c, data[0])
            phi_hat = get_phi_hat(c, data[2])  # Calculate phi_hat for each cutoff value
            theta = get_theta_hat(sensitivity, specificity, phi_hat)
            # Store the values in the lists
            sensitivity_values.append(sensitivity)
            specificity_values.append(specificity)
            theta_values.append(theta)
            # Calculate the Youden index for the current cutoff value and store it
            youden = get_youden_j_c(sensitivity, specificity)
            youden_values.append(youden)

        # Plot the Receiver Operating Characteristic (ROC) curve and the cutoff values
        plt.figure(figsize=(10, 6))
        # Plot J(c)
        plt.plot(norm_c_values, theta_values, label='Theta Hat Variation')
        # Find the index corresponding to the maximum Youden index
        max_youden_index = np.argmax(youden_values)
        # Plot the Youden choice point
        plt.scatter(norm_c_values[max_youden_index], theta_values[max_youden_index], color='red', label='Youden Choice')
    
        plt.xlabel('Normalized Cutoff Values')
        plt.ylabel('Theta Hat')
        plt.title('Theta Hat Variation with Normalized Cutoff Values')
        plt.legend()
        plt.ylim(0, 1)  # Set y-axis limits from 0 to 1
        plt.xlim(0, 1)  # Set x-axis limits from 0 to 1
        plt.savefig(args.output_file_theta)

    # Plotting function for just ELISA data!  
    fig, ax = plt.subplots(figsize=(10, 8))
    # Positive controls
    ax.scatter(np.random.normal(1, 0.05, len(data[0])), data[0], color='black', alpha=0.5, label='Positive Controls')
    # Negative controls
    ax.scatter(np.random.normal(2, 0.05, len(data[1])), data[1], color='red', alpha=0.5, label='Negative Controls')
    # Field data 
    ax.scatter(np.random.normal(3, 0.05, len(data[2])), data[2], color='blue', alpha=0.5, label='Field Data')
    ax.legend()
    ax.set_ylabel('ODs')
    ax.set_title('ELISA Data')
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(['Positive Controls', 'Negative Controls', 'Field Data'])
    plt.savefig(args.output_file_assay)
    
if __name__ == '__main__':
    main()
