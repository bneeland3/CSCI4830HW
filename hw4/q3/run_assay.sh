#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running assay data ...'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --output_file assay.png \
