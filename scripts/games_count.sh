#!/bin/bash
#
# This script is part of the Chess-AI GitHub project.
# It it used to get the number of all games in the saves directory.
#
saves_dir="${HOME}/saves"
count=0

# Print config and gamefile count
for folder in ${saves_dir}/*/
do
    files=$(ls ${folder}/*.pgn 2> /dev/null | wc -l || 0)
    count=$(expr $count + $files)
done

player=$(ls -t ${saves_dir}/*/*.pgn | head -1 | xargs grep White | cut -d'"' -f 2)
opponent=$(ls -t ${saves_dir}/*/*.pgn | head -1 | xargs grep Black | cut -d'"' -f 2)

if [[ -z "${player}" ]]; then
    echo "0:${count}:Last game: None"
else
    echo "0:${count}:Last game: ${player} vs ${opponent}"
fi
