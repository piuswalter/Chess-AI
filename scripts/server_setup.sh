#!/bin/bash
# simple script to setup a server. Tested with debian 11.
# Usage: curl <permalink> | sh

sudo apt-get update && sudo apt-get install -y podman nano unzip git curl wget jq tree
git clone https://github.com/piuswalter/chess-ai

mkdir -p ~/.config/containers
echo 'unqualified-search-registries = ["docker.io"]' > ~/.config/containers/registries.conf
cat > ~/.config/containers/containers.conf << EOF
[engine]
events_logger = "file"
cgroup_manager = "cgroupfs"
EOF

sudo mkdir -p /var/prtg/scripts/
curl https://raw.githubusercontent.com/piuswalter/Chess-AI/8c955a126304e30e73a208ab836dda71d2c7d6d6/scripts/games_count.sh | sudo tee /var/prtg/scripts/games_count.sh
sudo chmod +x /var/prtg/scripts/games_count.sh
