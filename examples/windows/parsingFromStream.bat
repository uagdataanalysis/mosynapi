:: Source: https://github.com/uagdataanalysis/mosynapi
:: Install MoSyn before execute this script.
::      pip install mosyn
:: Shows MoSyn Help

@echo off

echo "MoSyn Example: Parsing from stream."

cd ..

type "Poema20.txt" |  python -m mosyn >  "Poema20_morphological_stream.txt"

pause

@echo on