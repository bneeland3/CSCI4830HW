import sys
import sir
import numpy as np
import argparse
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
# from scipy.optimize import fsolve


def main():
    # The argparse library allows us to take command-lines arguments

    parser = argparse.ArgumentParser(
        description='passing parameters to the sir simulation using forward euler',
        prog='print sir simulation')

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
                    help='N value',
                    required=True)  # Adds argument for gamma value.

    parser.add_argument('--output_file',
                        type=str,
                        help='path for png or txt',
                        required=True)
    
    parser.add_argument('--r_infinity',
                        type=bool,
                        help='if you want to have r_infinity on the graph',
                        required=True)
    

    args = parser.parse_args()
    # Defines the command-line interface for the script
    data = sir.forward_euler_solver(args.beta, args.gamma, args.N)

    S = data[0]
    I = data[1]
    R = data[2]
    time = data[3]
    
    labels = ['S - Brenna', 'I - Brenna', 'R - Brenna']
    colors = ['blue', 'red', 'black']
        
    fig, ax = plt.subplots()
    if args.r_infinity == True:
        R_0 = args.beta/args.gamma
        r_infinity = fsolve(lambda r: r - (1-np.exp(-R_0*r)),0.5)[0]
        plt.axhline(y=r_infinity, color='green', linestyle='dotted',label=f'r_infinity = {r_infinity}')
    for i in range(3): # iterates through range
        ax.plot(time, data[i], label=labels[i], color=colors[i]) # plots varying parameters

    ax.set_title('SIR Model Simulation')
    ax.set_xlabel('Time')
    ax.set_ylabel('People')
    ax.set_xlim(left=0)
    
    ax.legend()
    plt.tight_layout()

    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
