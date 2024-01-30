import sys
import sir
import argparse
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def main():
    # The argparse library allows us to take command-lines arguments

    parser = argparse.ArgumentParser(
        description='passing parameters to the sir simulation using forward euler',
        prog='print sir simulation')

    parser.add_argument('--beta',
                        type=float,
                        help='Beta value',
                        required=True)  # Adds argument for the file_name.

    parser.add_argument('--gamma',
                        type=float,
                        help='Gamma value',
                        required=True)  # Adds argument for the file_name.

    parser.add_argument('--output_file',
                        type=str,
                        help='path for png or txt',
                        required=True)

    args = parser.parse_args()
    # Defines the command-line interface for the script
    data = sir.forward_euler_solver(args.beta, args.gamma)
    
    S = data[0]
    I = data[1]
    R = data[2]
    time = data[3]

    labels = ['Suceptible', 'Infected', 'Recovered']
    colors = ['blue', 'red', 'black']
    
    plt.figure(figsize=(10,6))
    
    for i in range(3):
        plt.plot(time, data[i], label=labels[i], color=colors[i])
        
    plt.title('SIR Model Simulation')
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.legenn()
    plt.grid(True)
    plt.show
    

if __name__ == '__main__':
    main()
