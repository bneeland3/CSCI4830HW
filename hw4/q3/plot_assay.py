import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
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
                        required=False) ##cutoff parameter, change in bash script
    
    parser.add_argument('--output_file',
                        type=str,
                        help='Output file name',
                        required=True)  
    
    args = parser.parse_args()
    
    # Read CSV files
    files = [args.pos_data, args.neg_data, args.field_data]
    data = read_csvs(files)
    
    if args.cutoff:
        specificity = get_sp(args.cutoff, data[0])
        sensitivity = get_se(args.cutoff, data[1])
        phi_hat = get_phi_hat(args.cutoff, data[2])
        j_c = get_youden_j_c(sensitivity, specificity)
        theta = get_theta_hat(sensitivity, specificity, phi_hat)
        print(f'Theta: {theta}')
        print(f'Youden J(c): {j_c}')
        
    fig, ax = plt.subplots(figsize=(10, 8))
    # positive controls
    ax.scatter(np.random.normal(1, 0.05, len(data[0])), data[0], color='black', alpha=0.5, label='Positive Controls')
    # negative controls
    ax.scatter(np.random.normal(2, 0.05, len(data[1])), data[1], color='red', alpha=0.5, label='Negative Controls')
    # field data 
    ax.scatter(np.random.normal(3, 0.05, len(data[2])), data[2], color='blue', alpha=0.5, label='Field Data')

    # Add legend
    ax.legend()
    # ax.set_xlabel('Samples')
    ax.set_ylabel('ODs')
    ax.set_title('ELISA Data')
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(['Positive Controls', 'Negative Controls', 'Field Data'])
    plt.savefig(args.output_file)
    
if __name__ == '__main__':
    main()
