
# Linux Installation

curl https://get.docker.com | sudo bash
# Add yourself to the docker group, the remote script suggested above will
# Have already created the docker group for you
sudo usermod -aG docker $(whoami)
# Restart the shell
