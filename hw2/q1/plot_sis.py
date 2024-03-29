import sis
import numpy as np
import argparse
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def main():
    # The argparse library allows us to take command-lines arguments

    parser = argparse.ArgumentParser(
        description='passing parameters to the sis simulation using forward euler',
        prog='print sis simulation')

    # argeparse arguements for bash script
    parser.add_argument('--beta',
                        type=float,
                        help='beta value',
                        required=True)  # Adds argument for beta value.

    parser.add_argument('--gamma',
                        type=float,
                        help='gamma value',
                        required=True)  # Adds argument for gamma value.
    
    parser.add_argument('--s_0',
                        type=float,
                        help='initial suceptibles',
                        required=True)  # Adds argument for gamma value.

    parser.add_argument('--i_0',
                        type=float,
                        help='initial infectious',
                        required=True)
    
    parser.add_argument('--delta_t',
                        type=float,
                        help='stepsize for delta_t',
                        required=True)
    
    parser.add_argument('--t_final',
                        type=int,
                        help='final num for time',
                        required=True)
    
    parser.add_argument('--output_file',
                        type=str,
                        help='name for file',
                        required=True)
    
    parser.add_argument('--E_delta_t',
                        type=bool,
                        help='returns absolute error',
                        required=False)

    # Defines the command-line interface for the script
    args = parser.parse_args()
    
    # function call and data declaration
    data = sis.forward_euler_solver(args.beta, args.gamma, args.s_0,
                                    args.i_0, args.delta_t, args.t_final)

    # S = data[0]
    I = data[1]
    time = data[2]
    analytical = data[3]
    
    fig, ax = plt.subplots()
    # Plot infected population with solid line
    ax.plot(time, I, color='red', label='Infected')
    # Plot analytical solution with dashed line
    ax.plot(time, analytical, color='black', label='Analytical', linestyle='--')
    
    if args.E_delta_t:
        absolute_error = sis.get_E_delta_t(args.beta, args.gamma, args.s_0, args.i_0, args.delta_t, args.t_final)
        print(round(absolute_error,6))

    ax.set_xlabel('Time')  # Set x-axis label
    ax.set_ylabel('Population')  # Set y-axis label to 'Population'
    ax.set_title('SIS Model Simulation')  # Set plot title
    ax.legend()  # Add legend
    plt.tight_layout()  # Adjust layout

    # Save plot to file
    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
