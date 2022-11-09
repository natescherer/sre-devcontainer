FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

# Set default shell for RUN commands to bash
SHELL ["/bin/bash", "-c"]

# Copy support files into image
COPY library/* /opt/sredevcontainer/

# # Install apt software
# RUN export DEBIAN_FRONTEND=noninteractive && \
#     apt update && \
#     xargs -r -L1 -a /opt/sredevcontainer/packages_apt.txt apt install -y && \
#     rm -rf /var/lib/apt/lists/* && \
#     unset DEBIAN_FRONTEND

# Set up shell profiles
# RUN sudo -u ${NONROOT_USER} mkdir -p /home/${NONROOT_USER}/.config/powershell && \
#     sudo -u ${NONROOT_USER} echo "python3 /opt/sredevcontainer/check_for_updates.py" >> /home/${NONROOT_USER}/.zshrc && \
#     sudo -u ${NONROOT_USER} echo "Start-Process -FilePath 'python3' -ArgumentList '/opt/sredevcontainer/check_for_updates.py' -Wait | Write-Warning" > /home/${NONROOT_USER}/.config/powershell/profile.ps1

# Install Python packages
# RUN pip3 --no-cache-dir install --upgrade pip && \
#     pip3 --no-cache-dir install -r /opt/sredevcontainer/requirements.txt

# Suppress Azure CLI noise
ENV AZSURVEYMESSAGE=false