FROM alpine

# Update packages and install python
RUN apk update && apk upgrade
RUN apk add python3 py-pip

# Insert run script in crontab
COPY cron-snippet etc/cron-snippet
WORKDIR /etc/
RUN cat cron-snippet >> ./crontabs/root

# Start CRON
CMD ["crond", "-f"]
