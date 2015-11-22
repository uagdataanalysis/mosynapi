Readme
November 21st, 2015
=======================

This directory contains examples that show how to use the Mosyn API.


parseFileSample.py
------------------
 - This is Python sample code that shows how to use the API to parse a plain 
text file. To execute it use the following line in the command prompt:
    python parseFileSample.py


parseStringSample.py
--------------------
 - This is Python sample code that shows how to use the API to parse text
in a String. To execute it use the following line in the command prompt:
    python parseStringSample.py
    
    
The following is an example of the output of both sample files above:
    " La " ( lema: el )
    	DA0FS0 -> singular female determinant 
	    PP3FSA00 -> singular female pronoun 
    ----------------------------------------------------

    " PUEDO " ( lema: poder )
	    VMIP1S0 -> singular verb without gender 
    ----------------------------------------------------
    
See the source code of those files in order to have a better understanding
of how to use the API.


    
    
Python Shell
=============
For Linux based O.S. there is a shell which is capable of executing python
code. Mosyn can be used that shell as well. Use the following syntax:

Show the help:

$ ./mosyn/mosyn.py -h
-------------- MoSyn Ver.1.0.3 --------------
Usage:
  mosyn [options]

General Options:
  -h, --help             Show help.
  -in, --input-file      Sets the input file.
  -out, --input-file     Sets the output file.
  -dict, --dictionary    Sets a dictionary file.
  

When executing without parameters Mosyn will show a shell prompt and will 
wait for the user to type a text in Spanish followed by enter:
    $ ./mosyn/mosyn.py 
    % La vida es bella.
    La |el|DA0FS0| |lo|PP3FSA00|
    vida |vida|NCFS000|
    es |ser|VMIP3S0|
    bella |bella|NP00000| |bello|AQ0FS0|
    . |.|FP|

The following is an example of how to parse an existing file:
    $ ./mosyn/mosyn.py -in test.txt 
    La |el|DA0FS0| |lo|PP3FSA00|
    vida |vida|NCFS000|
    es |ser|VMIP3S0|
    bella |bella|NP00000| |bello|AQ0FS0|

    
It is possible to send the output to a file using the following syntax:
    $ echo La vida es bella > test.txt
    $ ./mosyn/mosyn.py -in test.txt -out parsed.txt
    $ cat parsed.txt 
    La |el|DA0FS0| |lo|PP3FSA00|
    vida |vida|NCFS000|
    es |ser|VMIP3S0|
    bella |bella|NP00000| |bello|AQ0FS0|