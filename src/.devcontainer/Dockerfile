ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Copy support files into image
COPY .devcontainer/library/* /opt/sredevcontainer/

# Install apt software
RUN apt update && \
    bash /opt/sredevcontainer/powershell-debian.sh && \
    xargs -a /opt/sredevcontainer/packages_apt.txt apt install && \
    rm -rf /var/lib/apt/lists/*

# Install GitHub software
RUN source /opt/sredevcontainer/manual_install_functions.sh && \
    xargs -a /opt/sredevcontainer/packages_github.txt install_from_github

# Set up shell profiles
RUN sudo -u vscode mkdir -p /home/vscode/.config/powershell && \
    sudo -u vscode echo "python3 /opt/sredevcontainer/check_for_updates.py" >> /home/vscode/.zshrc && \
    sudo -u vscode echo "Start-Process -FilePath 'python3' -ArgumentList '/opt/sredevcontainer/check_for_updates.py' -Wait | Write-Warning" > /home/vscode/.config/powershell/profile.ps1

# Install Python packages
RUN pip3 --no-cache-dir install --upgrade pip && \
    pip3 --no-cache-dir install -r /opt/sredevcontainer/requirements.txt

# Install PowerShell modules
RUN pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted; Install-Module -Name (Get-Content /opt/sredevcontainer/requirements_pwsh.txt) -Scope AllUsers"