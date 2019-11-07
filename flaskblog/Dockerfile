FROM ubuntu:16.04
RUN apt-get update
RUN apt install python3-pip -y
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/bin/python3", "run.py"]
