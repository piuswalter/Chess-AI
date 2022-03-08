#!/bin/bash
# simple script to setup a server. Tested with debian 11.
# Usage: curl <permalink> | sh

sudo apt-get update && sudo apt-get install -y podman nano unzip git curl wget jq tree htop
git clone https://github.com/piuswalter/chess-ai

mkdir -p ~/.config/containers
echo 'unqualified-search-registries = ["docker.io"]' > ~/.config/containers/registries.conf
cat > ~/.config/containers/containers.conf << EOF
[engine]
events_logger = "file"
cgroup_manager = "cgroupfs"
EOF

sudo mkdir -p /var/prtg/scripts/
curl https://raw.githubusercontent.com/piuswalter/Chess-AI/f69e354a02dc3b150dc1e5e38bdd886b846b73f3/scripts/games_count.sh | sudo tee /var/prtg/scripts/games_count.sh
sudo chmod +x /var/prtg/scripts/games_count.sh

# Enable 4 GiB swap space
if ! [ -f /mnt/swapfile ]; then
  sudo fallocate --length 4GiB /mnt/swapfile
  sudo chmod 600 /mnt/swapfile
  sudo mkswap /mnt/swapfile
  sudo swapon /mnt/swapfile
  sudo sh -c 'echo "/mnt/swapfile swap swap defaults 0 0" >> /etc/fstab'
  sudo sh -c 'echo "vm.swappiness=10" >> /etc/sysctl.conf'
fi
