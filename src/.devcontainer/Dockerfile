FROM ubuntu:22.04

# Set default shell for RUN commands to bash
SHELL ["/bin/bash", "-c"]

# Copy support files into image
COPY library/* /opt/sredevcontainer/

# tzdata will prompt for input if not installed with the noninteractive switch
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

# Set up shell profiles
# RUN sudo -u ${NONROOT_USER} mkdir -p /home/${NONROOT_USER}/.config/powershell && \
#     sudo -u ${NONROOT_USER} echo "python3 /opt/sredevcontainer/check_for_updates.py" >> /home/${NONROOT_USER}/.zshrc && \
#     sudo -u ${NONROOT_USER} echo "Start-Process -FilePath 'python3' -ArgumentList '/opt/sredevcontainer/check_for_updates.py' -Wait | Write-Warning" > /home/${NONROOT_USER}/.config/powershell/profile.ps1
