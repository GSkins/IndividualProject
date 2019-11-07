#! /bin/sh
# make sure mysql is running
while ! nc -z mysql 3306; do
        echo "waiting for the db..."
        sleep 2
done
# create the tables if they don't exist
python3 create.py
# start the application
python3 run.py
