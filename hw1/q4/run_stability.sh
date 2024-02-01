#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot_stability.py when beta = 1 and gamma = 0.5...'
python plot_stability.py \
    --I 1 \
    --stable_R 0.9 \
    --unstable_R 1.1 \
    --gamma 0.5 \
    --N 1000000 \
    --output_file 'stability.png' \

