# use the Ubuntu Base Image
FROM ubuntu

# Set the Working Directory inside the container
WORKDIR /app

# Copy a script file to the container
COPY script.sh .

# Make the script executable 
RUN chmod +x script.sh

# Run the script when the container starts
CMD [ "./script.sh" ]