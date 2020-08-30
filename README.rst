.. image:: https://travis-ci.com/parisac/estc-parser.svg?branch=master
    :target: https://travis-ci.com/parisac/estc-parser


Welcome to estc-parser
######################
.. image:: ./static/estc.png
    width: 200pt
    height: 50pt

| This project was created to help academics and researchers more easily harvest book meta-data from the
|    `British Library English Short Title Catalogue "ESTC" <http://estc.bl.uk/F/QK6AUB9LGJYDXNE3FBT5KCHIDLR7KN7UTPFJKUCVH11FSCBCGQ-00698?func=file&file_name=find-b&local_base=BLL06>`_
|
| Currently if a researcher queries the short title catalog for a specific term, all results are only exportable as an *unstructured .html* file without table tags present. This project aims to simply an otherwise manual workflow by allowing the researcher to convert .html extracts into an *actionable* tabular .csv format.


Quickstart
==========
Supports Python >= 3.7.0

**Dump.html extracts**
**********
Place raw .html extract(s) in `./input_html`

**Poetry Usage**
*************************
estc-parser can be installed and run via `Poetry
<https://python-poetry.org/>`_,

.. code-block:: console

    cd estc-parser
    poetry install
    poetry run chewfiles

**Vanilla Python Usage**
****************************

.. code-block:: console

    cd estc-parser
    pip3 install -r requirements.txt
    python3 estc_parser/cli.py

**Grab Outputs**
*******************
Find .csv file with tabular results in `./output_csv`

Example Query
*************
After submitting a query a researcher can export results using the Email/print/save button highlighted below.

.. image:: ./static/chair.png
    :width: 200pt
    :height: 100pt

Example Raw Export
******************
Here is a sample of the raw unstructured .html export from our estc query.

.. image:: ./static/estc_raw.png
    :width: 200pt
    :height: 100pt

Transformed .csv Export via estc-parser
***************************************
Here we see the output of running the unstructured html above through estc-parser.

.. image:: ./static/tabular_csv.png
    :width: 200pt
    :height: 100pt
