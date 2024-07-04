FROM python:3.10.8-slim-buster
COPY requirements.txt .
RUN apt update -y && apt install git -y
RUN pip3 install -U -r requirements.txt
COPY . .
CMD ["/bin/bash", "/start.sh"]
echo "Starting DQ-The-File-Donor...."
python3 bot.py
