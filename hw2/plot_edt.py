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
    
    parser.add_argument('--graph_E',
                        type=bool,
                        help='returns absolute error',
                        required=False)

    # Defines the command-line interface for the script
    args = parser.parse_args()

    if args.E_delta_t:
        half_dt = sis.get_E_delta_t(args.beta,args.gamma,args.s_0,args.i_0,0.5,args.t_final)
        print(round(half_dt,6))
        
    if args.graph_E:
        # Run simulation for different step sizes to calculate E(delta_t)
        delta_ts = [2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125]
        errors = []
        for delta_t in delta_ts:
            error = sis.get_E_delta_t(args.beta, args.gamma, args.s_0,
                                    args.i_0, delta_t, args.t_final)
            errors.append(error)

    fig, ax = plt.subplots()
    ax.loglog(delta_ts, errors, marker='o', linestyle='-')
    ax.set_xlabel('Step size (delta_t)')
    ax.set_ylabel('Max Absolute Error (E(delta_t))')
    ax.set_title('Max Absolute Error vs. Step Size')
    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()