#!/bin/bash
PATH_TO_DOT="$(dirname "$(readlink -f "$0")")"
CLASSIC_COMMAND="python3 -m unittest discover "$PATH_TO_DOT/src""

if [[ "$1" == "-v" ]]
then
  CLASSIC_COMMAND="$CLASSIC_COMMAND -v"
fi

eval "$CLASSIC_COMMAND"
