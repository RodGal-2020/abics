#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`
# echo "\$PYTHONPATH = $PYTHONPATH"
# python check_files.py
python support/server.py
