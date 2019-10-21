export FLASK_APP=run.py
export FLASK_ENV=development

sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-venv

#git clone https://github.com/GSkins/flaskblog
cd ./Project/flaskblog/application
sudo mv -f venv ~/venv
python3 -m venv venv
. venv/bin/activate
cd ..
pip3 install flask
pip3 install SQLAlchemy
pip3 install flask_sqlalchemy
pip3 install WTForms
pip3 install flask-login
pip3 install flask-bcrypt
pip3 install flask_wtf
pip3 install DateTime
pip3 install PILLOW
pip install python-secrets
pip3 install python-secrets
pip install python2-secrets
pip3 install pyopenssl
#openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
#export FLASK_ENV=production FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 FLASK_RUN_CERT=cert.pem FLASK_RUN_KEY=key.pem
#flask run