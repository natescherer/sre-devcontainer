# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Copy support files into image
COPY .devcontainer/library/* /opt/sredevcontainer/

# Install Python packages
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /opt/sredevcontainer/requirements.txt

# Install Homebrew and Homebrew packages
ENV BREW_PREFIX=/home/linuxbrew/.linuxbrew
ENV PATH=${BREW_PREFIX}/sbin:${BREW_PREFIX}/bin:${PATH}
RUN apt-get update && bash /opt/sredevcontainer/homebrew-debian.sh automatic true true && \
brew install --ignore-dependencies kubectx && \
brew install k9s

# Install PowerShell and PowerShell modules
RUN apt-get update && bash /opt/sredevcontainer/powershell-debian.sh && \
pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted" && \
pwsh -c "Install-Module -Name (Get-Content /opt/sredevcontainer/requirements_pwsh.txt) -Scope AllUsers"

# Stop Azure CLI from asking about surveys
ENV AZURE_OUTPUT_SHOW_SURVEY_LINK=false