#!/bin/bash
#
# This script is part of the Chess-AI GitHub project.
# It it used to get a quick view of currently running
# statistics results and their containers.
#
saves_dir="../../saves"

echo -----------------------------------------------------------------------------------------------

# Print config and gamefile count
for folder in ${saves_dir}/*/
do
    cat ${folder}/meta 2> /dev/null
    count=$(ls ${folder}/*.pgn 2> /dev/null | wc -l)
    echo "Results in ${folder}:" $count
    echo ------------------------------------------
done

# Print container status
podman ps

echo -----------------------------------------------------------------------------------------------