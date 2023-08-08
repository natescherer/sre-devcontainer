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
        try:
            version = re.findall(regex, command_output)[0]
        except IndexError:
            version = "Regex Error"
            print(f"Regex error for '{command[0]}'")
    else:
        print(f"'{command[0]}' not found")
    return version


# PowerShell Resources
pwsh_resources = []
try:
    pwsh_resources = json.loads(subprocess.check_output(
        ["pwsh", "-NoProfile", "-c", "Get-PSResource -Scope AllUsers | "
         "Select-Object @{Name='Resources';Expression={$_.Name}}, "
         "@{Name='Version';Expression={$_.Version.ToString()}} | "
         "Sort-Object Tool | ConvertTo-Json"]).decode())
except subprocess.CalledProcessError:
    print("Error getting PowerShell resources.")

# Python Packages
py_packages = []
try:
    pip_output = subprocess.check_output(
        ["pip", "list", "--format", "json", "--disable-pip-version-check"]).decode()
    pip_array = json.loads(pip_output)
    py_packages = [{"Package": pkg["name"], "Version": pkg["version"]}
                   for pkg in pip_array]
except subprocess.CalledProcessError:
    print("Error getting Python packages.")

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
    # {
    #     "Technology": "Jupyter",
    #     "Tools": [
    #         {
    #             "Tool": "Jupyter Lab",
    #             "Version": get_tool_version(
    #                 ["jupyter", "lab", "--version"],
    #                 r"(\d+\.\d+\.\d+)")
    #         }
    #     ]
    # },
    {
        "Technology": "Kubernetes",
        "Tools": [
            {
                "Tool": "kubectl",
                "Version": get_tool_version(
                    ["asdf", "list", "kubectl", "|", "xargs", "sed", "'s/*//g'"],
                    r"(.*)")
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
            },
            {
                "Tool": "kubie",
                "Version": get_tool_version(
                    ["kubie", "-V"],
                    r"kubie (\d+\.\d+\.\d+)")
            }
        ]
    },
    {
        "Technology": "Networking",
        "Tools": [
            {
                "Tool": "dig",
                "Version": get_tool_version(
                    ["dig", "-v"],
                    r"DiG (\d+\.\d+\.\d+)")
            },
            {
                "Tool": "iputils-ping",
                "Version": get_tool_version(
                    ["ping", "-V"],
                    r"ping from iputils (\d+)")
            },
            {
                "Tool": "nslookup",
                "Version": get_tool_version(
                    ["nslookup", "-version"],
                    r"nslookup (\d+\.\d+\.\d+)")
            },
            {
                "Tool": "traceroute",
                "Version": get_tool_version(
                    ["traceroute", "-V"],
                    r"Modern traceroute for Linux, version (\d+\.\d+\.\d+)")
            },
        ]
    },
    {
        "Technology": "Python",
        "Tools": [
            {
                "Tool": "cookiecutter",
                "Version": get_tool_version(
                    ["cookiecutter", "-v"],
                    r"Cookiecutter (\d+\.\d+\.\d+)")
            },
            {
                "Tool": "nox",
                "Version": get_tool_version(
                    ["nox", "--version"],
                    r"(.*)")
            },
            {
                "Tool": "poetry",
                "Version": get_tool_version(
                    ["poetry", "-V"],
                    r"Poetry \(version (\d+\.\d+\.\d+)")
            },
            {
                "Tool": "Python",
                "Version": get_tool_version(
                    ["asdf", "list", "python", "|", "xargs", "sed", "'s/*//g'"],
                    r"(.*)")
            }
        ]
    },
    {
        "Technology": "Python Packages",
        "Tools": py_packages
    },
    {
        "Technology": "Shell Add-Ons: PowerShell Resources",
        "Tools": pwsh_resources
    },
    {
        "Technology": "Shells",
        "Tools": [
            {
                "Tool": "bash",
                "Version": get_tool_version(
                    ["bash", "--version"],
                    r"GNU bash, version (.*) ")
            },
            {
                "Tool": "PowerShell",
                "Version": get_tool_version(
                    ["pwsh", "--version"],
                    r"PowerShell (\d+\.\d+\.\d+)")
            },
            {
                "Tool": "zsh",
                "Version": get_tool_version(
                    ["zsh", "--version"],
                    r"zsh (\d+\.\d+\.\d+)")
            },
        ]
    },
    # {
    #     "Technology": "Terraform",
    #     "Tools": [
    #         {
    #             "Tool": "Terraform CLI",
    #             "Version": get_tool_version(
    #                 ["terraform", "-version"],
    #                 r"(\d+\.\d+\.\d+)")
    #         },
    #         {
    #             "Tool": "Terragrunt",
    #             "Version": get_tool_version(
    #                 ["terragrunt", "-v"],
    #                 r"(\d+\.\d+\.\d+)")
    #         },
    #         {
    #             "Tool": "TFLint",
    #             "Version": get_tool_version(
    #                 ["tflint", "-v"],
    #                 r"(\d+\.\d+\.\d+)")
    #         }
    #     ]
    # }
]

print(json.dumps(output_data, indent=4))

with open("ToolVersions.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)
