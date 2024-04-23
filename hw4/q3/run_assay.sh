#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running assay data with c = 13 ...'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --cutoff 13 \
    --output_file_assay assay.png 

echo '...running assay data with c = 17 ...'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --cutoff 17 \
    --output_file_assay assay.png 

echo '...running assay data with c = 15 ...'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --cutoff 15 \
    --output_file_assay assay.png 

echo '...running assay data and graphing ROC'
python plot_assay.py \
    --pos_data HW4_Q3_pos.csv \
    --neg_data HW4_Q3_neg.csv \
    --field_data HW4_Q3_data.csv \
    --output_file_assay assay.png \
    --output_file_roc roc.png \
    --output_file_theta theta.png
