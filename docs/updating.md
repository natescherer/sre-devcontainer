# Updating

- Close window
$x = docker ps --all --filter "ancestor=ghcr.io/natescherer/sre-devcontainer" --format "{{.Image}}"
docker pull $x
Open and Rebuild Container
docker image prune -f
