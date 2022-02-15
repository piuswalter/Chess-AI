#!/bin/bash
# Execute a given jupyter-notebook and handle runtime errors

if [ -z $1 ]; then
  echo "Usage: $0 <notebook>.ipynb"
  exit 1
fi

logfile="$(date +%s).log"
jupyter-execute --NbClientApp.log_level=DEBUG $1 2> ${logfile}

line_no=$(grep -n 'msg_type: error' ${logfile} | cut -d ':' -f 1)
if [[ "${line_no}" ]]; then
  tail --lines "+${line_no}" ${logfile}
  exit 1
fi
