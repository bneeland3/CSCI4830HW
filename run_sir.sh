#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running plot.py...'
python plot.py \
    --beta 1.0 \
    --gamma 0.5 \
    --output_file plot.png \