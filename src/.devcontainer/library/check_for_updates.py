"""Checks to see if there is a newer version of the SRE devcontainer
 released on GitHub"""
import semver
import requests
from rich import print # noqa

with open("/opt/sredevcontainer/VERSION", encoding="utf-8") as f:
    current_version = f.readlines()[0]

latest_version = requests.get(
    "https://raw.githubusercontent.com/natescherer/sre-devcontainer/main/LATESTVERSION").text # noqa

if (semver.compare(current_version, latest_version)) == -1:
    print("[reverse red]Current version of SRE devcontainer is out of date!"
        " Please run 'Rebuild and Reopen in Container' task in VSCode to"
        " update.[/reverse red]")
