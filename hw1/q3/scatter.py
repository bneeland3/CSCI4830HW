import sys
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from fsolve import find_f, find_g
from scipy.optimize import fsolve


def main():
    # The argparse library allows us to take command-lines arguments

    parser = argparse.ArgumentParser(
        description='passing parameters to the fsolve f and g functions',
        prog='print fsolve simulation')

    parser.add_argument('--output_file',
                        type=str,
                        help='path for png or txt',
                        required=True)

    args = parser.parse_args()
    # Defines the command-line interface for the script
    
    R_0_range = [0.9, 1.0, 1.1, 1.2]
    fig, axs = plt.subplots(2,2, figsize = (10,8))
    axs = axs.flatten()
    
    for i, R_0 in enumerate(R_0_range):
        r = np.linspace(0,1,100)
        f = find_f(r, R_0)
        g = find_g(r, R_0)
        
        axs[i].plot(r, f, color='red', label=f'f{r}')
        axs[i].plot(r, g, color = 'black', label=f'g{r}')
        
        point = fsolve(lambda r: find_f(r, R_0)-find_g(r, R_0), 0.5)[0]
        axs[i].scatter(point, find_f(point, R_0), color='blue', label ='intersection')
        
        axs[i].set_xlabel('r_infinity')
        axs[i].set_ylabel('value')
        axs[i].set_title(f'R_0 = {R_0}')
    
    fig.legend(labels=['f','g','intersection'], loc='upper right')
    plt.tight_layout()
    plt.savefig(args.output_file)

if __name__ == '__main__':
    main()
