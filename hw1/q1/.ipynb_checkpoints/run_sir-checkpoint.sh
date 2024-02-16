#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot.py when beta = 1 and gamma = 0.5...'
python plot.py \
    --beta 1.0 \
    --gamma 0.5 \
    --output_file 'beta1plot.png' \

echo '...running plot.py when beta = 1.5 and gamma = 0.5...'
python plot.py \
    --beta 1.5 \
    --gamma 0.5 \
    --output_file 'beta1.5plot.png' \
    
echo '...running plot.py when beta = 2 and gamma = 0.5...'
python plot.py \
    --beta 2.0 \
    --gamma 0.5 \
    --output_file 'beta2plot.png' \
    
