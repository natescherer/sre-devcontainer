ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Copy support files into image
COPY .devcontainer/library/* /opt/sredevcontainer/

# Call shell script to do installations to minimize layers
RUN bash /opt/sredevcontainer/install_sre_tools.sh