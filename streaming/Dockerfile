# gdelt-downloader-streaming
# Version: 0.2.1
# Description: Dockerfile for gdelt-downloader-streaming
# Author: github.com/yfiua

# Use the official Python base image
FROM python:3.12-slim

# Variables

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update and Install packages
RUN apt-get update -y \
        && apt-get install -y \
        curl \
        wget \
        unzip \
        cron

# Run cronjobs
RUN crontab gdelt-cronjobs

# Add stu
ADD https://github.com/yfiua/stu/releases/download/2.7.82/stu_amd64.deb stu_amd64.deb
RUN dpkg -i stu_amd64.deb
RUN rm stu_amd64.deb

# Ensure the script is executable
RUN chmod +x /app/*.py
RUN chmod +x /app/*.sh

RUN touch /var/log/cron.log

# Run the script by default when the container starts
CMD [ "sh", "-c", "cron && tail -f /var/log/cron.log" ]

