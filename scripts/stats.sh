#!/bin/bash -e
#
# This script is part of the Chess-AI GitHub project.
# It it used to generate a statistics table for
# different AI versions with the given parameters.
#
proj_dir="$(readlink -f $(dirname $0))/.."

players='Exercise01AI, Exercise02AI, Exercise03AI, Exercise04AI, StockfishPlayer'
opponents='Exercise01AI, Exercise02AI, Exercise03AI, Exercise04AI, StockfishPlayer'
seed=3
repetitions=1
depth=3

if command -v podman >/dev/null 2>&1; then
    cmd="podman"
else
    cmd="docker"
fi

timestamp=$(date +%s)
savedir="${HOME}/saves/${timestamp}"
mkdir -p "${savedir}"
echo "Date: $(date)" > "${savedir}"/meta
echo "players=${players}" >> "${savedir}"/meta
echo "opponents=${opponents}" >> "${savedir}"/meta
echo "seed=${seed}" >> "${savedir}"/meta
echo "repetitions=${repetitions}" >> "${savedir}"/meta
echo "depth=${depth}" >> "${savedir}"/meta

$cmd run --rm \
    -e player="${players}" \
    -e opponents="${opponents}" \
    -e seed="${seed}" \
    -e repetitions="${repetitions}" \
    -e depth="${depth}" \
    -v "${proj_dir}:/app:z" \
    -v "${savedir}:/app/games:Z" \
    --name "chess_stats_${timestamp}" \
    --log-opt "path=${savedir}/container.log" \
    -d python:3.10.1 bash -c "
        pip install notebook -r /app/src/requirements.txt
        echo 'Running statistics notebook'
        jupyter-execute /app/src/Statistics.ipynb
    "
