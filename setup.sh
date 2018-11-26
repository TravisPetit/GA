#!/bin/bash

dir=$(pwd -P)/src
echo export PYTHONPATH=${PYTHONPATH}:$dir >> ~/.bashrc
