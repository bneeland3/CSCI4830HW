#!/bin/bash
set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot_sir.py with R_0 = 5...'
python plot_sir.py \
    --R_0 5.0 \
    --N 300000 \
    --VE 0.8 \
    --output_file r05.png \

echo '...running plot_sir.py with R_0 = 4..'
python plot_sir.py \
    --R_0 4.0 \
    --N 300000 \
    --VE 0.8 \
    --output_file r04.png \

echo '...running plot_sir.py with R_0 = 3...'
python plot_sir.py \
    --R_0 3.0 \
    --N 300000 \
    --VE 0.8 \
    --output_file r03.png \

# Testing framework
echo '...running plot_sir.py with VE = 0...'
python plot_sir.py \
    --R_0 4.0 \
    --N 300000 \
    --VE 0.0 \
    --output_file ve0.png \

echo '...running plot_sir.py with VE = 1...'
python plot_sir.py \
    --R_0 4.0 \
    --N 300000 \
    --VE 1.0 \
    --output_file ve1.png \