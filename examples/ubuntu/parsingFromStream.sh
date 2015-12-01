#!/bin/bash

# Source: https://github.com/uagdataanalysis/mosynapi
# Install MoSyn before execute this script.
#      pip install mosyn
# Use application streams to provide information to MoSyn.

cd ..

echo "MoSyn Example: Parsing from stream."

cat "Poema20.txt" |  python -m mosyn |  "Poema20_morphological_stream.txt"
