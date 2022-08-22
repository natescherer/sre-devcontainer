ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Copy support files into image
COPY .devcontainer/library/* /opt/sredevcontainer/

# Set up zsh and pwsh profiles
RUN cat /opt/sredevcontainer/profile >> /home/vscode/.zshrc && \
    mkdir -p /home/vscode/.config/powershell && \
    cat /opt/sredevcontainer/profile > /home/vscode/.config/powershell/profile.ps1

# Install Python packages
RUN pip3 --no-cache-dir install --upgrade pip && \
    pip3 --no-cache-dir install -r /opt/sredevcontainer/requirements.txt

# Install Homebrew and Homebrew packages
ENV PATH=/home/linuxbrew/.linuxbrew/sbin:/home/linuxbrew/.linuxbrew/bin:${PATH}
RUN apt-get update && \
    export USE_SHALLOW_CLONE="true" && \
    bash /opt/sredevcontainer/homebrew-debian.sh automatic true true && \
    unset USE_SHALLOW_CLONE && \
    brew install --ignore-dependencies kubectx && \
    brew install k9s && \
    rm -rf /var/lib/apt/lists/*

# Install PowerShell and PowerShell modules
RUN apt-get update && bash /opt/sredevcontainer/powershell-debian.sh && \
    pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted" && \
    pwsh -c "Install-Module -Name (Get-Content /opt/sredevcontainer/requirements_pwsh.txt) -Scope AllUsers" && \
    rm -rf /var/lib/apt/lists/*

# Stop Azure CLI from asking about surveys
ENV AZURE_OUTPUT_SHOW_SURVEY_LINK=false