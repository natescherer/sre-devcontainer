#!/usr/bin/env bash

ARGUMENT_LIST=(
  "repo"
  "filename-template"
  "version"
  "version-prefix"
  "dest-folder"
  "binary-name"
)

# read arguments
opts=$(getopt \
  --longoptions "$(printf "%s:," "${ARGUMENT_LIST[@]}")" \
  --name "$(basename "$0")" \
  --options "" \
  -- "$@"
)

eval set --$opts

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      repo=$2
      shift 2
      ;;

    --filename-template)
      filenameTemplate=$2
      shift 2
      ;;

    --version)
      version=$2
      shift 2
      ;;

    --version-prefix)
      versionPrefix=$2
      shift 2
      ;;

    --dest-folder)
      destFolder=$2
      shift 2
      ;;

    --binary-name)
      binaryName=$2
      shift 2
      ;;

    *)
      break
      ;;
  esac
done

find_github_release_asset_url() {
    local repo=$1
    local filenameTemplate=$2
    local version=$3
    local versionPrefix=${4:-"v"}

    if [ "${version}" = "latest" ]; then
        version=$(find_latest_version_from_git_tags https://github.com/${repo})
    fi
    arch="$(dpkg --print-architecture)"
    if [ "${arch}" = "amd64" ]; then
        arch="(amd64|x64|x86_64)"
    fi

    local filename=${filenameTemplate/VERSION/"${version}"}
    filename=${filename/ARCH/"${arch}"}
    local downloadUrl=$(curl -H "Accept: application/vnd.github+json" -s https://api.github.com/repos/${repo}/releases/tags/${versionPrefix}${version} | jq -r -c ".assets[] | select(.name|test(\"${filename}\")) | .browser_download_url")

    echo $downloadUrl
}

find_latest_version_from_git_tags() {
    local repoUrl=$1
    local versionPrefix=${2:-"tags/v"}
    local separator=${3:-"."}
    local last_part_optional=${4:-"false"}

    local escaped_separator=${separator//./\\.}
    local last_part
    if [ "$last_part_optional" = "true" ]; then
        last_part="($escaped_separator[0-9]+)?"
    else
        last_part="$escaped_separator[0-9]+"
    fi
    local regex="$versionPrefix\\K[0-9]+$escaped_separator[0-9]+$last_part$"
    local version_list="$(git ls-remote --tags $repoUrl | grep -oP "$regex" | tr -d ' ' | tr "$separator" "." | sort -rV)"

    latestVersion="$(echo "$version_list" | head -n 1)"
    echo $latestVersion
}

download_and_install_gzipped_tarball() {
    local url=$1
    local destFolder=$2
    local binaryName=$3

    local installTempPath=/tmp/ghinstall
    local tarballName=$(echo "$url" | rev | cut -d'/' -f1 | rev)

    echo "Installing $url to $destFolder..."

    mkdir -p "$installTempPath" "/opt/$binaryName"
    curl -sSL -o "$installTempPath/$tarballName" "$url"
    tar xf "$installTempPath/$tarballName" -C "$destFolder"
    ln -s "$destFolder/$binaryName" "/usr/local/bin/$binaryName"
    rm -rf "$installTempPath"
}

ghUrl="$(find_github_release_asset_url $repo $filenameTemplate $version $versionPrefix)"

download_and_install_gzipped_tarball $ghUrl $destFolder $binaryName