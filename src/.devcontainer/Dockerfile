# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY .devcontainer/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Install Homebrew and Homebrew packages
ENV BREW_PREFIX=/home/linuxbrew/.linuxbrew
ENV PATH=${BREW_PREFIX}/sbin:${BREW_PREFIX}/bin:${PATH}
COPY .devcontainer/library-scripts/homebrew-debian.sh /tmp/library-scripts/
RUN apt-get update && bash /tmp/library-scripts/homebrew-debian.sh automatic true true
RUN brew install --ignore-dependencies kubectx
RUN brew install k9s

# Install PowerShell and PowerShell modules
COPY .devcontainer/library-scripts/powershell-debian.sh /tmp/library-scripts/
RUN apt-get update && bash /tmp/library-scripts/powershell-debian.sh
COPY .devcontainer/requirements_pwsh.txt /tmp/pwsh-tmp/
RUN pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted"
RUN pwsh -c "Install-Module -Name (Get-Content /tmp/pwsh-tmp/requirements_pwsh.txt) -Scope AllUsers"

# Stop Azure CLI from asking about surveys
ENV AZURE_OUTPUT_SHOW_SURVEY_LINK=false

# Load in scripts custom to this container
COPY .devcontainer/versioninfo.py /opt/sredevcontainer/