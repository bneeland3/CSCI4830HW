#!/bin/bash
set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot_edt.py without graph...'
python plot_edt.py \
    --beta 3.0 \
    --gamma 2.0 \
    --s_0 0.99 \
    --i_0 0.01 \
    --delta_t 0.5 \
    --t_final 25 \
    --output_file E_delta_t.png \
    --E_delta_t True \
    --graph_E False \

echo '...running plot_edt.py with graph...'
python plot_edt.py \
    --beta 3.0 \
    --gamma 2.0 \
    --s_0 0.99 \
    --i_0 0.01 \
    --delta_t 0.5 \
    --t_final 25 \
    --output_file E_delta_t.png \
    --E_delta_t False \
    --graph_E True \