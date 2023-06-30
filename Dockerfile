# Base Image
FROM python:3.10

ARG ANSIBLE_VERSION=8.1.0

# Install Ansible version 8.1.0
RUN pip install ansible==$ANSIBLE_VERSION

# Create directory
RUN mkdir -p /vish-ansible

# Set the working directory
WORKDIR /vish-ansible

# Run the container continuosly without exiting
CMD ["/bin/bash", "-c", "tail -f /dev/null"]