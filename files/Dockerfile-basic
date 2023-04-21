FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

ENV FLASK_APP=back.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
