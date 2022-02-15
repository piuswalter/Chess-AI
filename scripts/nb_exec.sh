#!/bin/bash
# Execute a given jupyter-notebook and handle runtime errors

if [ -z $1 ]; then
  echo "Usage: $0 <notebook>.ipynb"
  exit 1
fi

tempfile=$(mktemp)
jupyter-execute --NbClientApp.log_level=DEBUG $1 2> ${tempfile}

line_no=$(grep -n 'msg_type: error' ${tempfile} | cut -d ':' -f 1)
if [[ "${line_no}" ]]; then
  tail --lines "+${line_no}" ${tempfile}
  exit 1
fi

rm ${tempfile}
