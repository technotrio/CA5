# Using Jenkins as a base image
FROM jenkins/jenkins:lts

USER root

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Docker
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io

# Add the jenkins user to the docker group
RUN usermod -aG docker jenkins

# Switch back to the jenkins user
USER jenkins

# Configure the Python application
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app

# Define the entry point for your Python application
CMD python app.py

# Expose the necessary port for your Python application (if required)
# EXPOSE 5000
