FROM python:3.8-alpine

# Update packages and install dependencies
RUN apk update && apk upgrade
RUN apk add g++ 

# Install requirements
WORKDIR /app/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Insert run script in crontab
COPY cron-snippet /etc/cron-snippet
WORKDIR /etc/
RUN cat cron-snippet >> ./crontabs/root

# Copy application code
WORKDIR /app/
COPY ./src/ ./src/

# Start CRON
CMD ["crond", "-f"]
