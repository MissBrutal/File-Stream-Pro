FROM python:3.11

WORKDIR /app
COPY . /app
COPY hold.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD python -m Filestream && python hold.py
