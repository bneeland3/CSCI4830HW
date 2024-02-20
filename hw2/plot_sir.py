import numpy as np
import argparse
import matplotlib.pyplot as plt
import mod_sir

def main():
    # The argparse library allows us to take command-line arguments

    parser = argparse.ArgumentParser(
        description='Passing parameters to the SIR simulation using Forward Euler',
        prog='print SIR simulation')

    # argparse arguments for bash script
    parser.add_argument('--beta',
                        type=float,
                        help='Beta value',
                        required=True)  # Adds argument for beta value.

    parser.add_argument('--gamma',
                        type=float,
                        help='Gamma value',
                        required=True)  # Adds argument for gamma value.
    
    parser.add_argument('--N',
                        type=int,
                        help='Population size',
                        required=True)

    parser.add_argument('--R_0',
                        type=float,
                        help='Basic reproduction number',
                        required=False)

    parser.add_argument('--output_file',
                        type=str,
                        help='Name for file',
                        required=True)

    # Defines the command-line interface for the script
    args = parser.parse_args()
    
    # Function call and data declaration
    time, susceptibles, infected, recovered = mod_sir.forward_euler_solver(args.beta, args.gamma, args.N, args.R_0)

    # Plotting
    plt.plot(time, susceptibles, color='blue', label='Susceptible')
    plt.plot(time, infected, color='red', label='Infected')
    plt.plot(time, recovered, color='green', label='Recovered')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.title('SIR Model Simulation (Forward Euler)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot to file
    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
