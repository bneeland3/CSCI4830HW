#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running assay data with c = 15 ...'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --cutoff 15 \
    --output_file assay.png 

echo '...running assay data with c = 13 ...'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --cutoff 13 \
    --output_file assay.png 
