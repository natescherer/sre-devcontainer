# Updating

- Close window
- $x = docker ps --all --filter "ancestor=ghcr.io/natescherer/sre-devcontainer" --format "{{.Image}}"
- docker pull $x
- Rebuild
- docker image prune -f