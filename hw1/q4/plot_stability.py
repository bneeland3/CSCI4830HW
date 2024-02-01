import sys
import stability
import argparse
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def main():
    # The argparse library allows us to take command-lines arguments

    parser = argparse.ArgumentParser(
        description='passing parameters to the sir simulation using forward euler',
        prog='print sir simulation')
    
    parser.add_argument('--I',
                    type=float,
                    help='R value',
                    required=True)  # Adds argument for stable R_0 value.

    parser.add_argument('--stable_R',
                        type=float,
                        help='R value',
                        required=True)  # Adds argument for stable R_0 value.
    
    parser.add_argument('--unstable_R',
                    type=float,
                    help='R value',
                    required=True)  # Adds argument for stable R_0 value.

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

    

    args = parser.parse_args()
    # Defines the command-line interface for the script
    epsilon = 1/args.N
    S = args.N - epsilon
    
    stable_data = stability.forward_euler_solver(S, args.I, args.stable_R, args.gamma, args.N)
    unstable_data = stability.forward_euler_solver(S, args.I, args.unstable_R, args.gamma, args.N)
    
    stable_s = stable_data[0]
    stable_i = stable_data[1]
    stable_r = stable_data[2]
    time = stable_data[3]
    
    unstable_s = unstable_data[0]
    unstable_i = unstable_data[1]
    unstable_r = unstable_data[2]
    
    
    stable_labels = ['S - stable', 'I - stable', 'R - stable',]
    stable_colors = ['blue', 'red', 'black']
    
    unstable_labels = ['S - unstable', 'I - unstable', 'R - unstable' ]
    unstable_colors = ['green','yellow','pink']
        
    fig, ax = plt.subplots()

    for i in range(3): # iterates through rante
        ax.plot(time, stable_data[i], label=stable_labels[i], color=stable_colors[i]) # plots varying parameters
        ax.plot(time, unstable_data[i], label=unstable_labels[i], color=unstable_colors[i])
        
    ax.set_title('SIR Model Simulation')
    ax.set_xlabel('Time')
    ax.set_ylabel('People')
    ax.set_xlim(left=0)
    
    ax.legend()
    plt.tight_layout()

    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
