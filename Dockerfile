FROM python:3.13-slim

WORKDIR /parking_service

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install -y libglib2.0-0 libnspr4 libnss3 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libexpat1 libatspi2.0-0 libx11-6 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 libgbm1 libxcb1 libxkbcommon0 libasound2

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install

EXPOSE 8000
