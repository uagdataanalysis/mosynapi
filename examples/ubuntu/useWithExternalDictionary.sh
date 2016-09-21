#!/bin/bash

# Source: https://github.com/uagdataanalysis/mosynapi
# Install MoSyn before execute this script.
#      pip install mosyn
# MoSyn Example: Using an external dictionary.

echo "MoSyn Example: Using an external dictionary."

cd ..

python -m mosyn --input-file "Poema20.txt" --output-file "Poema20_morphological.txt" --dictionary "../mosyn/dict/spanish_dict.csv"
