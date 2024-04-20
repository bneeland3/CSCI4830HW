import argparse
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from assay import read_csvs 

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
    
    parser.add_argument('--output_file',
                        type=str,
                        help='Output file name',
                        required=True)  
    
    args = parser.parse_args()
    
    # Read CSV files
    files = [args.pos_data, args.neg_data, args.field_data]
    all_data = read_csvs(files)

    custom_palette = {0: 'black', 1: 'red', 2: 'blue'}  
    sns.scatterplot(data=all_data,palette=custom_palette)
    plt.xlabel('Samples')
    plt.ylabel('ODs')
    plt.title('ELISA Scatter Plot')
    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
