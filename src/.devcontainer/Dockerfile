FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye

ARG username=vscode

# Set default shell for RUN commands to bash
SHELL ["/bin/bash", "-c"]

# Copy support files into image
COPY .devcontainer/library/* /opt/sredevcontainer/

# # Install apt software
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt update && \
    bash /opt/sredevcontainer/powershell-debian.sh && \
    xargs -r -L1 -a /opt/sredevcontainer/packages_apt.txt apt install -y && \
    rm -rf /var/lib/apt/lists/* && \
    unset DEBIAN_FRONTEND

# Install GitHub software
RUN xargs -r -L1 -a /opt/sredevcontainer/packages_github.txt bash /opt/sredevcontainer/install_from_github.sh

# Set up shell profiles
RUN sudo -u ${username} mkdir -p /home/${username}/.config/powershell && \
    sudo -u ${username} echo "python3 /opt/sredevcontainer/check_for_updates.py" >> /home/${username}/.zshrc && \
    sudo -u ${username} echo "Start-Process -FilePath 'python3' -ArgumentList '/opt/sredevcontainer/check_for_updates.py' -Wait | Write-Warning" > /home/${username}/.config/powershell/profile.ps1

# Install Python packages
RUN pip3 --no-cache-dir install --upgrade pip && \
    pip3 --no-cache-dir install -r /opt/sredevcontainer/requirements.txt

# Install PowerShell modules
RUN pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted" && \
    pwsh -c "Install-Module -Name (Get-Content /opt/sredevcontainer/requirements_pwsh.txt) -Scope AllUsers"

# Suppress Azure CLI noise
ENV AZURE_OUTPUT_SHOW_SURVEY_LINK=false