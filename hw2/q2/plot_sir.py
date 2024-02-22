import numpy as np
import argparse
import matplotlib.pyplot as plt
from mod_sir import forward_euler_solver_lm, forward_euler_solver_anm

def main():
    # The argparse library allows us to take command-line arguments

    parser = argparse.ArgumentParser(
        description='Passing parameters to the SIR simulation using Forward Euler',
        prog='print SIR simulation')

    # argparse arguments for bash script
    
    parser.add_argument('--R_0',
                        type=float,
                        help='Basic reproduction num',
                        required=True)

    parser.add_argument('--N',
                        type=int,
                        help='population size',
                        required=True)
    
    parser.add_argument('--VE',
                        type=float,
                        help='vaccine efficacy',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='Name for file',
                        required=True)

    # Defines the command-line interface for the script
    args = parser.parse_args()
    
    # Function call and data declaration
    lm_data = forward_euler_solver_lm(args.R_0, args.N, args.VE)
    anm_data = forward_euler_solver_anm(args.R_0, args.N, args.VE)

    
    fig, ax = plt.subplots()
    ax.plot(lm_data[0], lm_data[2], color='red', label='Infected-LM')
    ax.plot(anm_data[0], anm_data[2], color='blue', label='Infected-ANM')
    ax.set_xlabel('Time')
    ax.set_ylabel('Infected Population')
    ax.set_title(f'Infected Population in SIR Model Simulation of {args.R_0}')
    ax.legend()
    plt.tight_layout()

    # Save plot to file
    fig.savefig(args.output_file)

if __name__ == '__main__':
    main()
