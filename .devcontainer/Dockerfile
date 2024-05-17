# Use the specified Python image from Microsoft Container Registry
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye


# Install Node.js, npm, and yarn
RUN apt-get update && apt-get install -y nodejs npm yarn curl gpg

RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg;
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null;
RUN apt-get update && apt-get install -y  gh

RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt /tmp

# Install Python dependencies
RUN python3 -m pip install -r /tmp/requirements.txt


