FROM python:3
RUN yes | apt-get update
RUN yes | apt-get install python3-pip
RUN pip install flask
WORKDIR /app
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3", "api.py"]
