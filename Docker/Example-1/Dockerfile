FROM ubuntu:latest

#Set working Directory in the Image
WORKDIR /app

# Copy the files from the host file system to image file system.
COPY . /app

# Install Necessary Packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Set Env Variables
ENV NAME World

# Run a Command to start the app
CMD ["python3", "app.py"]

