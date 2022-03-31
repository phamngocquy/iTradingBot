#!/bin/bash

pylint --rcfile=./.pylintrc --fail-under=6 src
