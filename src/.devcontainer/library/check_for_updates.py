"""Checks to see if there is a newer version of the SRE devcontainer
 released on GitHub"""
import sys
import requests
import semver
from rich import print # pylint: disable=redefined-builtin

# with open("/opt/sredevcontainer/VERSION", encoding="utf-8") as f:
#     current_version = f.readlines()[0]

current_version = "0.0.0"

api_uri = "https://api.github.com/repos/natescherer/sre-devcontainer/releases/latest"
try:
    api_response = requests.get(api_uri, timeout=10).json()
except requests.exceptions.ConnectionError:
    print("[reverse red]Error connecting to GitHub to check for SRE "
          "devcontainer updates. Make sure your internet connection is "
          "working.[/reverse red]")
    sys.exit(1)

latest_version = api_response["tag_name"].replace("v","")

if (semver.compare(current_version, latest_version)) == -1:
    print("[reverse red]Current version of SRE devcontainer is out of date!"
        " Please run 'Rebuild and Reopen in Container' task in VSCode to"
        " update.[/reverse red]")
