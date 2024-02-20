#!/bin/bash
set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot_sir.py under vaccination models...'
python plot_sir.py \
    --beta 3.0 \
    --gamma 2.0 \
    --N 300000 \
    --R_0 3.0 \
    --output_file sir_simulation.png
