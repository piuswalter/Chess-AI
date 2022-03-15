#!/bin/bash -e
#
# This script is part of the Chess-AI GitHub project.
# It it used to generate a statistics table for
# different AI versions with the given parameters.
#
proj_dir="$(readlink -f $(dirname $0))/.."

config="$(cat ${proj_dir}/scripts/config.json)"


if command -v podman >/dev/null 2>&1; then
    cmd="podman"
else
    cmd="docker"
fi

timestamp=$(date +%s)
savedir="${HOME}/saves/${timestamp}"
mkdir -p "${savedir}"
echo "Date: $(date)" > "${savedir}"/meta
echo "config=${config}" >> "${savedir}"/meta


$cmd run --rm \
    -e config="${config}" \
    -e CI="true" \
    -v "${proj_dir}:/app:z" \
    -v "${savedir}:/app/games:Z" \
    --name "chess_stats_${timestamp}" \
    --log-opt "path=${savedir}/container.log" \
    -d python:3.10.1 bash -c "
        pip install notebook -r /app/src/requirements.txt
        echo 'Running statistics'
        # Convert notebooks
        jupyter nbconvert --to python \
        --output-dir=/app/python \
        --TemplateExporter.extra_template_basedirs=/app/scripts \
        --template nbconverter_template \
        /app/src/*.ipynb
        # Run converted statistics notebook
        cd /app/python
        python Statistics.py
    "
