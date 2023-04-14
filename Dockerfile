# Draw base image from Python 3.11.3 Image in DHub
FROM python:3.11.3

# This line sets an environment variable in the container. 
# The PYTHONUNBUFFERED variable is set to 1, which means that 
# Python will run in unbuffered mode. This can be helpful when 
# running your application in a container, as it ensures that Python's 
# output is immediately visible and not buffered
ENV PYTHONUNBUFFERED=1

# This line sets the working directory for the following instructions 
# in the Dockerfile. In this case, it creates a directory named /app 
# in the container and sets it as the working directory.
WORKDIR /app

# This line copies the pyproject.toml and poetry.lock files from the project directory 
# on the host machine to the /app directory in the container. 
# These files are needed for Poetry to manage dependencies.
COPY pyproject.toml poetry.lock /app/

# Configures Poetry and instructs it not to create virtual environments, 
# as they are not needed in a Docker container.
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

# Copies the contents of the app to the container
COPY . /app

# This line specifies the default command to run when a container 
# is started from the image. In this case, it runs Gunicorn, 
# a WSGI HTTP server, to serve the Django application.
CMD ["gunicorn", "spms.wsgi:application", "--bind", "0.0.0.0:8000"]
