"""Gets versions of tools that are part of the SRE devcontainer"""
import json
import re
import subprocess
from shutil import which


def get_tool_version(command, regex):
    """Gets a version of a command line tool"""
    version = "Not Found"
    if which(command[0]):
        command_output = subprocess.check_output(command).decode()
        version = re.findall(regex, command_output)[0]
    else:
        print(f"'{command[0]}' not found")
    return version


# PowerShell Resources
pwsh_resources = json.loads(subprocess.check_output(
    ["pwsh", "-NoProfile", "-c", "Get-PSResource -Scope AllUsers | "
     "Select-Object @{Name='Resources';Expression={$_.Name}},Version | "
     "Sort-Object Tool | ConvertTo-Json"]).decode())

# Python Packages
pip_output = subprocess.check_output(
    ["pip3", "list", "--format", "json", "--disable-pip-version-check"]).decode()
pip_array = json.loads(pip_output)
py_packages = [{"Package": pkg["name"], "Version": pkg["version"]}
               for pkg in pip_array]

output_data = [
    {
        "Technology": "AWS",
        "Tools": [
            {
                "Tool": "AWS CLI",
                "Version": get_tool_version(
                    ["aws", "--version"],
                    r"aws-cli\/(\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "Azure",
        "Tools": [
            {
                "Tool": "Azure CLI",
                "Version": get_tool_version(
                    ["az", "--version", "--only-show-errors"],
                    r"azure-cli\s*(\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "Git",
        "Tools": [
            {
                "Tool": "Git",
                "Version": get_tool_version(
                    ["git", "--version"],
                    r"git version (\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "GitHub",
        "Tools": [
            {
                "Tool": "GitHub CLI",
                "Version": get_tool_version(
                    ["gh", "--version"],
                    r"gh version (\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "Jupyter",
        "Tools": [
            {
                "Tool": "Jupyter Lab",
                "Version": get_tool_version(
                    ["jupyter", "lab", "--version"],
                    r"(\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "Kubernetes",
        "Tools": [
            {
                "Tool": "kubectl",
                "Version": get_tool_version(
                    ["kubectl", "version", "--client", "--output=yaml"],
                    r"gitVersion: v(\d+\.\d+\.\d+)")
            },
            {
                "Tool": "Helm",
                "Version": get_tool_version(
                    ["helm", "version", "--short"],
                    r"v(\d+\.\d+\.\d+)")
            },
            {
                "Tool": "k9s",
                "Version": get_tool_version(
                    ["k9s", "version", "-s"],
                    r"Version\s+v(\d+\.\d+\.\d+)")
            },
            {
                "Tool": "kubectx",
                "Version": get_tool_version(
                    ["kubectx", "--version"],
                    r"(\d+\.\d+\.\d+)")
            },
            {
                "Tool": "kubens",
                "Version": get_tool_version(
                    ["kubens", "--version"],
                    r"(\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "PowerShell",
        "Tools": [
            {
                "Tool": "PowerShell",
                "Version": get_tool_version(
                    ["pwsh", "--version"],
                    r"PowerShell (\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "PowerShell Resources",
        "Tools": pwsh_resources
    },
    {
        "Technology": "Python",
        "Tools": [
            {
                "Tool": "Python",
                "Version": get_tool_version(
                    ["pwsh", "--version"],
                    r"Python (\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "Python Packages",
        "Tools": py_packages
    },
    {
        "Technology": "Terraform",
        "Tools": [
            {
                "Tool": "Terraform CLI",
                "Version": get_tool_version(
                    ["terraform", "-version"],
                    r"(\d+\.\d+\.\d+)")
            },
            {
                "Tool": "Terragrunt",
                "Version": get_tool_version(
                    ["terragrunt", "-v"],
                    r"(\d+\.\d+\.\d+)")
            },
            {
                "Tool": "TFLint",
                "Version": get_tool_version(
                    ["tflint", "-v"],
                    r"(\d+\.\d+\.\d+)")
            }
        ]
    }
]

print(json.dumps(output_data))
