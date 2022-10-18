"""Gets versions of tools that are part of the SRE devcontainer"""
import subprocess
import json

# AWS
aws_raw = subprocess.run(
    ["aws", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
aws_ver = aws_raw.splitlines()[0].split(" ")[0].split("/")[1]


# Azure
az_raw = subprocess.run(
    ["az", "--version", "--only-show-errors"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
az_ver = az_raw.splitlines()[0].split(" ")[-1]


# Git
git_raw = subprocess.run(
    ["git", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
git_ver = git_raw.splitlines()[0].split(" ")[-1]


# GitHub
gh_raw = subprocess.run(
    ["gh", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
gh_ver = gh_raw.splitlines()[0].split(" (")[0].split(" ")[-1]


# Jupyter
# jup_raw = subprocess.run(
#     ["jupyter", "lab", "--version"],
#     check=True,
#     stdout=subprocess.PIPE
# ).stdout.decode("utf-8")
# jup_ver = jup_raw.splitlines()[0]


# Kubernetes
helm_raw = subprocess.run(
    ["helm", "version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
helm_ver = helm_raw.splitlines()[0].split("Version:\"v")[1].split("\"")[0]

k9s_raw = subprocess.run(
    ["k9s", "version", "-s"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
k9s_ver = k9s_raw.splitlines()[0].split(" ")[-1]

kubectl_raw = subprocess.run(
    ["kubectl", "version", "--short"],
    check=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
).stdout.decode("utf-8")
kubectl_ver = kubectl_raw.splitlines()[0].split(" v")[1]

kubectx_raw = subprocess.run(
    ["kubectx", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
kubectx_ver = kubectx_raw.splitlines()[0]

kubens_raw = subprocess.run(
    ["kubens", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
kubens_ver = kubens_raw.splitlines()[0]


# PowerShell
pwsh_raw = subprocess.run(
    ["pwsh", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
pwsh_ver = pwsh_raw.splitlines()[0].split(" ")[1]


# PowerShell Modules
# pwsh_modules_json = subprocess.run(
#     ["pwsh", "-NoProfile", "-c", "Get-InstalledModule | "
#      "Select-Object @{Name='Tool';Expression={$_.Name}},Version | "
#      "Sort-Object Tool | ConvertTo-Json"
#      ],
#     check=True,
#     stdout=subprocess.PIPE
# ).stdout.decode("utf-8")
# pwsh_modules = json.loads(pwsh_modules_json)


# Python
py_raw = subprocess.run(
    ["python", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
py_ver = py_raw.splitlines()[0].split(" ")[1]


# Python Packages
pip_json = subprocess.run(
    ["pip3", "list", "--format", "json"],
    check=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
).stdout.decode("utf-8")
pip_array = json.loads(pip_json)
py_packages = []
for pkg in pip_array:
    py_packages.append({
        "Tool": pkg["name"],
        "Version": pkg["version"]
    })


# Terraform
tf_raw = subprocess.run(
    ["terraform", "-version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
tf_ver = tf_raw.splitlines()[0].split(" v")[1]

terragrunt_raw = subprocess.run(
    ["terragrunt", "-v"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
terragrunt_ver = terragrunt_raw.splitlines()[0].split(" v")[-1]

tflint_raw = subprocess.run(
    ["tflint", "-v"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
tflint_ver = tflint_raw.splitlines()[0].split(" ")[-1]


output_data = [
    {
        "Technology": "AWS",
        "Tools": [
            {
                "Tool": "AWS CLI",
                "Version": aws_ver
            },
            {
                "Tool": "boto3 Python Package",
                "Version": [x for x in py_packages
                            if x["Tool"] == "boto3"][0]["Version"]
            }
        ]
    },
    {
        "Technology": "Azure",
        "Tools": [
            # {
            #     "Tool": "Az PowerShell Module",
            #     "Version": [x for x in pwsh_modules
            #                 if x["Tool"] == "Az"][0]["Version"]
            # },
            {
                "Tool": "Azure CLI",
                "Version": az_ver
            }
        ]
    },
    {
        "Technology": "Git",
        "Tools": [
            {
                "Tool": "Git",
                "Version": git_ver
            }
        ]
    },
    {
        "Technology": "GitHub",
        "Tools": [
            {
                "Tool": "GitHub CLI",
                "Version": gh_ver
            }
        ]
    },
    # {
    #     "Technology": "Jupyter",
    #     "Tools": [
    #         {
    #             "Tool": "Jupyter Lab",
    #             "Version": jup_ver
    #         }
    #     ]
    # },
    {
        "Technology": "Kubernetes",
        "Tools": [
            {
                "Tool": "Helm",
                "Version": helm_ver
            },
            {
                "Tool": "k9s",
                "Version": k9s_ver
            },
            {
                "Tool": "kubectl",
                "Version": kubectl_ver
            },
            {
                "Tool": "kubectx",
                "Version": kubectx_ver
            },
            {
                "Tool": "kubens",
                "Version": kubens_ver
            }
        ]
    },
    {
        "Technology": "PowerShell",
        "Tools": [
            {
                "Tool": "PowerShell",
                "Version": pwsh_ver
            }
        ]
    },
    # {
    #     "Technology": "PowerShell Modules",
    #     "Tools": pwsh_modules
    # },
    {
        "Technology": "Python",
        "Tools": [
            {
                "Tool": "Python",
                "Version": py_ver
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
                "Version": tf_ver
            },
            {
                "Tool": "Terragrunt",
                "Version": terragrunt_ver
            },
            {
                "Tool": "TFLint",
                "Version": tflint_ver
            }
        ]
    }
]

print(json.dumps(output_data))
