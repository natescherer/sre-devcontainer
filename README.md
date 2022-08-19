# SRE Dev Container

This project builds a VSCode/GitHub Codespaces Dev Container optimized for Site Reliability Engineering workflows.

This container is built upon Microsoft's [python-3](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3) container, meaning it is Debian 11 "bullseye" with support for x86-64 and arm64 (including Apple M-series processors).

The container includes tooling for the below technologies, sorted alphabetically:

(NOTE: All tools included in the image are the latest stable releases available at build time. If you have a need for an earlier version, such as an older version of Python, please open an issue!)

- AWS
  - AWS CLI
  - AWS.Tools.Common PowerShell module
- Azure
  - Az PowerShell module
  - Azure CLI
- Git
  - Git
- GitHub
  - GitHub CLI
- Jupyter
  - JupyterLab
- Kubernetes
  - Helm
  - k9s
  - kubectl
  - kubectx
  - kubens
- PowerShell
  - LTS-current release
  - Includes PowerShell modules useful to SREs (full list available under [releases](releases))
- Python
  - Latest stable release
  - Includes Python packages useful to SREs (full list available under [releases](releases))
- SSH
  - OpenSSH Client
  - OpenSSH Server
- Terraform
  - Terraform CLI
  - TFLint
  - Terragrunt
- VSCode Extensions
  - Code Spell Checker (streetsidesoftware.code-spell-checker)
  - git-autoconfig (shyykoserhiy.git-autoconfig)
  - Intellicode (visualstudioexptteam.vscodeintellicode)
  - Jupyter (ms-toolsai.jupyter)
  - Jupyter Keymap (ms-toolsai.jupyter-keymap)
  - Jupyter Notebook Renderers (ms-toolsai.jupyter-renderers)
  - Kubernetes (ms-kubernetes-tools.vscode-kubernetes-tools)
  - markdownlint (davidanson.vscode-markdownlint)
  - PowerShell (ms-vscode.powershell)
  - Pylance (ms-python.vscode-pylance)
  - Python (ms-python.python)
  - YAML (redhat.vscode-yaml)

## Getting Started

This container is compatible with GitHub Codespaces in the cloud, and locally with VSCode on Windows/macOS/Linux with x86-64 or arm64 processors.

### Prerequisites

For VSCode Remote Containers, ensure you have followed the initial setup instructions [here](https://code.visualstudio.com/docs/remote/containers).

For GitHub Codespaces, no prerequisites are needed.

### Installing

TBD

## Usage

### Examples

TBD

### Documentation

For detailed documentation, [click here on GitHub](docs).

## Questions/Comments

If you have questions, comments, etc, please enter a GitHub Issue with the "question" tag.

## Contributing/Bug Reporting

Contributions and bug reports are gladly accepted! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Building

All builds are automated via GitHub Actions. If you fork this repository, you should also be able to build using the same Actions.

## Authors

**Nate Scherer** - *Initial work* - [natescherer](https://github.com/natescherer)

## License

This project is licensed under The MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgements

[Microsoft](https://github.com/microsoft/vscode-dev-containers) - For providing the Dev Container architecture and the base images used in this project
