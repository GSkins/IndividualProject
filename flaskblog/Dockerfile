FROM ubuntu:16.04
RUN apt-get update
RUN apt install python3-pip -y
COPY . .
RUN pip3 install -r IndividualProject/flaskblog/requirements.txt
WORKDIR IndividualProject/flaskblog
ENTRYPOINT ["python3", "run.py"]
