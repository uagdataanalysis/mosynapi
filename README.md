# Morpho-Syntactic "MoSyn" API
## UAG - BIG DATA RESEARCH GROUP
----
### Description
This API has been created by the Universidad Autónoma de Guadalajara(UAG) Big Data Research Group as a Natural Language Processing tool. It provides a python library with functions that help to perform morphological anaysis on texts written in Spanish.

 - Quick overview on what morphological analysis is in the following video: [El análisis morfológico de una oración](https://www.youtube.com/watch?v=BgAHya5ejJ8)
 - Link to EAGLES standard:[INTRODUCCIÓN A LAS ETIQUETAS EAGLES](http://www.cs.upc.edu/~nlp/tools/parole-sp.html) 
----
## Installation
The following packages are required to install mosyn
 - Python: [https://www.python.org/](https://www.python.org/)
 - PyPI: [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

Once having installed the depenencies above then install mosyn:
```
# pip install mosyn
```

If at any point the following error appears:
```python
Resource u'tokenizers/punkt/english.pickle' not found.  Please
use the NLTK Downloader to obtain the resource:

    >>>nltk.download()

Searched in:
- '/home/ec2-user/nltk_data'
- '/usr/share/nltk_data'
- '/usr/local/share/nltk_data'
- '/usr/lib/nltk_data'
- '/usr/local/lib/nltk_data'
- u''
```
try the instructions in the following link:
[http://stackoverflow.com/questions/26570944/resource-utokenizers-punkt-english-pickle-not-found](http://stackoverflow.com/questions/26570944/resource-utokenizers-punkt-english-pickle-not-found)


## Running examples
Examples are provided in the installation package. They are copied as part of mosyn installation. Use the command `pydoc mosyn´ in order to find the directory where mosyn was installed, e.g.:
```
$ pydoc mosyn
```

After hit enter a screen with a text similar to the following should appear:
```
Help on package mosyn:

NAME
    mosyn - # -*- coding: iso-8859-15 -*-

FILE
    /Library/Python/2.7/site-packages/mosyn-1.0.5-py2.7.egg/mosyn/__init__.py

PACKAGE CONTENTS
    __main__
    mosyn
    util (package)

(END)
```

In that example mosyn is installed in `/Library/Python/2.7/site-packages/mosyn-1.0.5-py2.7.egg/mosyn`. Navigate to that directory and execute one of the examples:


## Contact
Please address questions to uag-data-analysis@googlegroups.com

Report a bug by creating an issue in the following link:
[https://github.com/uagdataanalysis/mosynapi/issues](https://github.com/uagdataanalysis/mosynapi/issues)


<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
