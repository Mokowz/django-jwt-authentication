FROM python:3.8.3-slim-buster

# Set up the workdir
WORKDIR /auth/djw-auth-1

# Set up environmental variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip

# Install the dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the whole project
COPY . .

# Expose the port 
EXPOSE 8000

# Command to start the image
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]