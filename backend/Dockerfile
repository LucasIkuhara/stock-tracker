FROM python:3.8-alpine

# Update packages and install dependencies
RUN apk update && apk upgrade
RUN apk add g++ 

# Install requirements
WORKDIR /app/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy application code
COPY ./src/ ./src/
