# IndividualProject

To start it up:

#! /bin/bash

gcloud compute instances create test --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud --zone europe-west2-a

gcloud compute ssh test -q --zone europe-west2-a --project gskinstestproject << EOF
sudo apt-get update -y
sudo apt install python3-pip -y
git clone https://github.com/GSkins/IndividualProject
pip3 install -r IndividualProject/flaskblog/requirements.txt
python3 ./IndividualProject/flaskblog/run.py
EOF
