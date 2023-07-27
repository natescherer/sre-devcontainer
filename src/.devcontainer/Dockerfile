FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Set default shell for RUN commands to bash
SHELL ["/bin/bash", "-c"]

# Copy support files into image
COPY library/* /opt/sredevcontainer/

# tzdata will prompt for input if not installed with the noninteractive switch
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*