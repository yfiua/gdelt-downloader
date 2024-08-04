# gdelt-downloader
# Version: 0.1.1
# Description: Dockerfile for gdelt-downloader
# Author: github.com/yfiua

# Use the official Python base image
FROM python:3.12-slim

# Variables
ENV n_jobs 1
ENV start_date 19700101
ENV end_date 99991231

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update and Install packages
RUN apt-get update -y \
        && apt-get install -y \
        wget \
        unzip

# Add stu
ADD https://github.com/yfiua/stu/releases/download/2.7.82/stu_amd64.deb stu_amd64.deb
RUN dpkg -i stu_amd64.deb

# Ensure the script is executable
RUN chmod +x /app/*.py

# Run the script by default when the container starts
CMD [ "sh", "-c", "echo ${start_date} > START_DATE && echo ${end_date} > END_DATE && stu -j ${n_jobs}" ]
