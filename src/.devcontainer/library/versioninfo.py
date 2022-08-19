import subprocess
import json

print("AWS")
aws_raw = subprocess.run(
    ["aws", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
aws_ver = aws_raw.splitlines()[0].split(" ")[0].split("/")[1]
print(f"| AWS CLI | {aws_ver} |")

print("Azure")
az_raw = subprocess.run(
    ["az", "--version", "--only-show-errors"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
az_ver = az_raw.splitlines()[0].split(" ")[-1]
print(f"| Azure CLI | {az_ver} |")

print("Git")
git_raw = subprocess.run(
    ["git", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
git_ver = git_raw.splitlines()[0].split(" ")[-1]
print(f"| Git | {git_ver} |")

print("GitHub")
gh_raw = subprocess.run(
    ["gh", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
gh_ver = gh_raw.splitlines()[0].split(" (")[0].split(" ")[-1]
print(f"| GitHub CLI | {gh_ver} |")

print("Jupyter")
jup_raw = subprocess.run(
    ["jupyter", "lab", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
jup_ver = jup_raw.splitlines()[0]
print(f"| Jupyter Lab | {jup_ver} |")

print("Kubernetes")
helm_raw = subprocess.run(
    ["helm", "version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
helm_ver = helm_raw.splitlines()[0].split("Version:\"v")[1].split("\"")[0]
print(f"| Helm | {helm_ver} |")
k9s_raw = subprocess.run(
    ["k9s", "version", "-s"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
k9s_ver = k9s_raw.splitlines()[0].split(" ")[-1]
print(f"| k9s | {k9s_ver} |")
kubectl_raw = subprocess.run(
    ["kubectl", "version", "--short"],
    check=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
).stdout.decode("utf-8")
kubectl_ver = kubectl_raw.splitlines()[0].split(" v")[1]
print(f"| kubectl | {kubectl_ver} |")
kubectx_raw = subprocess.run(
    ["brew", "list", "--versions", "kubectx"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
kubectx_ver = kubectx_raw.splitlines()[0].split(" ")[1]
print(f"| kubectx | {kubectx_ver} |")
print(f"| kubens | {kubectx_ver} |")

print("PowerShell")
pwsh_raw = subprocess.run(
    ["pwsh", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
pwsh_ver = pwsh_raw.splitlines()[0].split(" ")[1]
print(f"| PowerShell | {pwsh_ver} |")
mod_json = subprocess.run(
    ["pwsh", "-c", "Get-InstalledModule | "
     "Select-Object Name,Version | "
     "Sort-Object Name | ConvertTo-Json"
     ],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
mod_array = json.loads(mod_json)
for mod in mod_array:
    print(f"| PowerShell Module: {mod['Name']} | {mod['Version']} |")

print("Python")
py_raw = subprocess.run(
    ["python", "--version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
py_ver = py_raw.splitlines()[0].split(" ")[1]
print(f"| Python | {py_ver} |")
pkg_json = subprocess.run(
    ["pip3", "list", "--format", "json"],
    check=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
).stdout.decode("utf-8")
pkg_array = json.loads(pkg_json)
for pkg in pkg_array:
    print(f"| Python Package: {pkg['name']} | {pkg['version']} |")

print("SSH")
ssh_raw = subprocess.run(
    ["ssh", "-V"],
    check=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
).stderr.decode("utf-8")
ssh_ver = ssh_raw.splitlines()[0].split("_")[1].split(" ")[0]
print(f"| OpenSSH Client | {ssh_ver} |")
print(f"| OpenSSH Server | {ssh_ver} |")

print("Terraform")
tf_raw = subprocess.run(
    ["terraform", "-version"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
tf_ver = tf_raw.splitlines()[0].split(" v")[1]
print(f"| Terraform CLI | {tf_ver} |")
tflint_raw = subprocess.run(
    ["tflint", "-v"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
tflint_ver = tflint_raw.splitlines()[0].split(" ")[-1]
print(f"| TFLint | {tflint_ver} |")
terragrunt_raw = subprocess.run(
    ["terragrunt", "-v"],
    check=True,
    stdout=subprocess.PIPE
).stdout.decode("utf-8")
terragrunt_ver = terragrunt_raw.splitlines()[0].split(" v")[-1]
print(f"| Terragrunt | {terragrunt_ver} |")
