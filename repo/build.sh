#!/bin/bash
dpkg-scanpackages -m  debs/ > Packages;
python generateDepiction.py
bzip2 -fks Packages;