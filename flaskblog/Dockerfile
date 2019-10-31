FROM ubuntu:16.04
RUN apt-get update
RUN apt install python3-pip -y
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "run.py"]
