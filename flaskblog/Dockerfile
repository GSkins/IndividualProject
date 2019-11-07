FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install build-essential libssl-dev libffi-dev python-dev -y
RUN apt install python3-pip -y
RUN apt install -y netcat
COPY ./requirements.txt .
RUN pip3 install PyMySQL[rsa]
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["./init.sh"]
