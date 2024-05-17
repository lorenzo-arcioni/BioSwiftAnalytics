#!/bin/bash

tar --exclude "results/*.png" --exclude "results/*.xlsx" -cvzf bioswiftanalytics.tar.gz data notebooks results fasta.py fasta2karyotype.py dockerfile requirements.txt README.md