#!/usr/bin/env bash

# Install apt-get software
apt-get update
bash /opt/sredevcontainer/powershell-debian.sh
rm -rf /var/lib/apt/lists/*

# Install manual software
source /opt/sredevcontainer/manual_install_functions.sh
install_from_github ahmetb kubectx kubectx_vVERSION_linux_ARCH.tar.gz /opt/kubectx/kubectx
install_from_github ahmetb kubectx kubens_vVERSION_linux_ARCH.tar.gz /opt/kubens/kubens
install_from_github derailed k9s k9s_Linux_ARCH.tar.gz /opt/k9s/k9s

# Set up zsh and pwsh profiles
sudo -u vscode mkdir -p /home/vscode/.config/powershell
local UPDATE_SCRIPT="python3 /opt/sredevcontainer/check_for_updates.py"
local UPDATE_SCRIPT_ZSH="${UPDATE_SCRIPT} > 2>&1"
local UPDATE_SCRIPT_PWSH="${UPDATE_SCRIPT} > 1>&3"
sudo -u vscode echo $UPDATE_SCRIPT >> /home/vscode/.zshrc
sudo -u vscode echo $UPDATE_SCRIPT > /home/vscode/.config/powershell/profile.ps1

# Install Python packages
pip3 --no-cache-dir install --upgrade pip
pip3 --no-cache-dir install -r /opt/sredevcontainer/requirements.txt

# Install PowerShell modules
pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted"
pwsh -c "Install-Module -Name (Get-Content /opt/sredevcontainer/requirements_pwsh.txt) -Scope AllUsers"