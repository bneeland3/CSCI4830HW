#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot_sis.py when delta_t = 2 ...'
python plot_sis.py \
    --beta 3.0 \
    --gamma 2.0 \
    --s_0  0.99 \
    --i_0  0.01 \
    --delta_t 2.0 \
    --t_final 25 \
    --output_file delt_t2.png \

echo '...running plot_sis.py when delta_t = 1 ...'
python plot_sis.py \
    --beta 3.0 \
    --gamma 2.0 \
    --s_0  0.99 \
    --i_0  0.01 \
    --delta_t 1.0 \
    --t_final 25 \
    --output_file delt_t1.png \

echo '...running plot_sis.py when delta_t = 0.5 ...'
python plot_sis.py \
    --beta 3.0 \
    --gamma 2.0 \
    --s_0  0.99 \
    --i_0  0.01 \
    --delta_t 0.5 \
    --t_final 25 \
    --output_file delt_t0.5.png \

