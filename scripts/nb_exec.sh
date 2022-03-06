#!/bin/bash
# Execute a given jupyter-notebook and handle runtime errors

if [ -z $1 ]; then
  echo "Usage: $0 <notebook>.ipynb"
  exit 1
fi

if [ -d "games" ]; then
  logfile="$(date +%s).log"
else
  logfile="/app/games/$(date +%s).log"
fi
jupyter-execute --NbClientApp.log_level=DEBUG $1 2> ${logfile}

line_no=$(grep -n -e 'Kernel died' -e 'msg_type: error' ${logfile} | head -1 | cut -d ':' -f 1)
if [[ "${line_no}" ]]; then
  tail --lines "+${line_no}" ${logfile}
  exit 1
fi
