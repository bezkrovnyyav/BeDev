FROM python:3.10.7-alpine3.16

RUN apk update && apk upgrade

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD ["python", "chatbot.py"]