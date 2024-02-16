import sys
import argparse
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from stability import forward_euler_solver


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
                        type=float,
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
    
    stable_data = forward_euler_solver(S, args.I, args.stable_R, args.gamma, args.N)
    unstable_data = forward_euler_solver(S, args.I, args.unstable_R, args.gamma, args.N)
    
    stable_s, stable_i, stable_r, time = stable_data
    unstable_s, unstable_i, unstable_r, _ = unstable_data 
    
    
#     stable_labels = ['S - stable', 'I - stable', 'R - stable',]
#     stable_colors = ['blue', 'red', 'black']
    
#     unstable_labels = ['S - unstable', 'I - unstable', 'R - unstable' ]
#     unstable_colors = ['green','yellow','pink']
        
    plt.figure(figsize =(10,6))

#     for i in range(3): # iterates through rante
#         ax.plot(time, stable_data[i], label=stable_labels[i], color=stable_colors[i]) # plots varying parameters
#         ax.plot(time, unstable_data[i], label=unstable_labels[i], color=unstable_colors[i])
        
    plt.plot(time, stable_s, color = 'red', label = 'S stable equilibrium', linestyle ='dotted')
    plt.plot(time, stable_i, color= 'blue',label = 'I stable equilibrium', linestyle ='dotted')
    plt.plot(time, stable_r, color = 'black', label = 'R stable equilibrium', linestyle ='dotted')
    
    plt.plot(time, unstable_s, color = 'yellow', label = 'S unstable equilibrium', linestyle ='dashed')
    plt.plot(time, unstable_i, color= 'pink', label = 'I unstable equilibrium', linestyle ='dashed')
    plt.plot(time, unstable_r, color = 'green', label = 'R unstable equilibrium', linestyle ='dashed')
    
    plt.title('SIR Model Simulation')
    plt.xlabel('Time')
    plt.ylabel('People')
    # plt.set_xlim(left=0)
    
    plt.legend()
    # plt.tight_layout()

    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
