#!/bin/bash

set -e # -e stops on error.
set -u # -u raises error.
set -o pipefail # Fails if a prior step has failed.

echo '...running scatter.py...'
python scatter.py \
    --output_file plots.png