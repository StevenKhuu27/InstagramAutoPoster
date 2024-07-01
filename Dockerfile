# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "./app.py"]