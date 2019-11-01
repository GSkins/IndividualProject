# Introduction
>This is my bucket list website

>I have been using ubuntu 16.04 LTS on a vm in gcp


# Pre Requisites

>sudo apt-get update  
>#check you have python3 installed  
>sudo apt-get install python3-pip -y  
>sudo apt-get install python3-venv -y  


# Running the app on a local machine  

>git clone https://github.com/GSkins/IndividualProject  
>python3 -m venv venv  
>. venv/bin/activate  
>export FLASK_APP=run.py  
>export FLASK_ENV=development  
>cd flaskblog/  
>pip3 install -r requirements.txt  
>pip3 install pyopenssl  
>openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365  
>python3 run.py  

# Execute shell for Jenkins

>sudo apt-get update  
>sudo apt-get install python3-pip -y  
>sudo apt-get install python3-venv -y  

>#under source code management use git - https://github.com/GSkins/IndividualProject  

>#move to module folder  
>cd ./flaskblog  
>#install the service script  
>sudo cp flask-app.service /etc/systemd/system/  
>#reload the service scripts  
>sudo systemctl daemon-reload  
>#stop the old service  
>sudo systemctl stop flask-app  
>#install the application files  
>install_dir=/opt/flask-app  
>sudo rm -rf ${install_dir}  
>sudo mkdir ${install_dir}  
>sudo cp -r ./* ${install_dir}  
>sudo chown -R pythonadm:pythonadm ${install_dir}  
>#configure python virtual environment and install dependencies  
>sudo su - pythonadm << EOF  
>cd ${install_dir}  
>virtualenv -p python3 venv  
>source venv/bin/activate  
>pip3 install virtualenv  
>pip3 install -r requirements.txt  
>EOF  


# Execute shell for Docker  

>cd ./flaskblog  
>sudo docker build -t flask-app .  
>if sudo docker ps -a | grep flask-app;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; then sudo docker rm -f flask-app  
>fi  
>sudo docker run -d -p 5000:5000 --name flask-app flask-app  
