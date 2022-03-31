#!/bin/bash

pylint --rcfile=./.pylintrc --fail-under=8 src
