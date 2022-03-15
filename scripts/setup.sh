#!/bin/bash -e
#
# This script is part of the Chess-AI GitHub project.
# It it used to setup a Linux environment to be ready to run all Chess-AI notebooks.
#
STOCKFISH_VERSION="${STOCKFISH_VERSION:-14.1}"
lib_dir="$(readlink -f $(dirname $0))/../lib"

# Install stockfish
stockfish=stockfish_${STOCKFISH_VERSION}_linux_x64
wget https://stockfishchess.org/files/${stockfish}.zip
unzip ${stockfish}.zip
mv ${stockfish}/${stockfish} ${lib_dir}/stockfish/stockfish.exe
rm -r ${stockfish}{,.zip}
chmod +x ${lib_dir}/stockfish/stockfish.exe

# Fetch endgame library
wget --execute="robots = off" --mirror --convert-links --no-parent http://tablebase.sesse.net/syzygy/3-4-5/
mv tablebase.sesse.net/syzygy/3-4-5/*.{rtbz,rtbw,md5} ${lib_dir}/ending/3-4-5/
rm -r tablebase.sesse.net
cd ${lib_dir}/ending/3-4-5/ && md5sum -c checksum.md5
