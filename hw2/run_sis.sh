#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot_sis.py...'
python plot_sis.py \
    --beta 3.0 \
    --gamma 2.0 \
    --s_0  0.99 \
    --i_0  0.01 \
    --delta_t 2 \
    --t_final 25 \
    --output_file delt_t2.png \


