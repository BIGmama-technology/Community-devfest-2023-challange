# Use the official Python image as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .
RUN pip install .

# Expose the port that the application will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]