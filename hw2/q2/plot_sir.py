import numpy as np
import argparse
import matplotlib.pyplot as plt
from mod_sir import forward_euler_solver_lm, forward_euler_solver_anm

def main():
    parser = argparse.ArgumentParser(
        description='Passing parameters to the SIR simulation using Forward Euler',
        prog='print SIR simulation')

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

    args = parser.parse_args()
    
    # Run LM and ANM simulations
    lm_data = forward_euler_solver_lm(args.R_0, args.N, args.VE)
    anm_data = forward_euler_solver_anm(args.R_0, args.N, args.VE)
    
    # Extract cumulative infectious populations
    lm_cumulative_infectious = round(lm_data[5], 0)  # Last value of infected from LM data
    anm_cumulative_infectious = round(anm_data[6], 0)  # Last value of infected from ANM data
    
    print(f'Cumulative infectious for LM: {lm_cumulative_infectious}')
    print(f'Cumulative infectious for ANM: {anm_cumulative_infectious}')
    
    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # SIR dynamic curves 
    ax1.plot(lm_data[0], lm_data[2], color='red', label='Infected-LM')
    ax1.plot(anm_data[0], anm_data[2], color='blue', label='Infected-ANM')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Infected Population')
    ax1.set_title(f'Infected Population in SIR Model Simulation of {args.R_0}')
    ax1.legend()

    # Bar Plots
    ax2.bar(['LM', 'ANM'], [lm_cumulative_infectious, anm_cumulative_infectious], color=['red', 'blue'])
    ax2.set_ylabel('Cumulative Infectious Population')
    ax2.set_title('Cumulative Infectious Population')
    
    plt.tight_layout()

    # Save plot to file
    fig.savefig(args.output_file)

if __name__ == '__main__':
    main()
