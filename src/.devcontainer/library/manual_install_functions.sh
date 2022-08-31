#!/usr/bin/env bash

find_github_release_asset_url() {
    local owner=$1
    local repo=$2
    local release_asset_format=$3
    local version=${4}
    local versionprefix=${5:-"v"}

    if [ "${version}" = "latest" ]; then
        version=$(find_latest_version_from_git_tags https://github.com/${owner}/${repo})
    fi
    arch="$(dpkg --print-architecture)"
    if [ "${arch}" = "amd64" ]; then
        arch="(amd64|x64|x86_64)"
    fi

    local filename=${release_asset_format/VERSION/"${version}"}
    filename=${filename/ARCH/"${arch}"}
    local download_url=$(curl -H "Accept: application/vnd.github+json" -s https://api.github.com/repos/${owner}/${repo}/releases/tags/${versionprefix}${version} | jq -r -c ".assets[] | select(.name|test(\"${filename}\")) | .browser_download_url")

    echo $download_url
}

find_latest_version_from_git_tags() {
    local repository=$1
    local prefix=${2:-"tags/v"}
    local separator=${3:-"."}
    local last_part_optional=${4:-"false"}

    local escaped_separator=${separator//./\\.}
    local last_part
    if [ "${last_part_optional}" = "true" ]; then
        last_part="(${escaped_separator}[0-9]+)?"
    else
        last_part="${escaped_separator}[0-9]+"
    fi
    local regex="${prefix}\\K[0-9]+${escaped_separator}[0-9]+${last_part}$"
    local version_list="$(git ls-remote --tags ${repository} | grep -oP "${regex}" | tr -d ' ' | tr "${separator}" "." | sort -rV)"

    LATEST_VERSION="$(echo "${version_list}" | head -n 1)"
    echo $LATEST_VERSION
}

download_and_install_gzipped_tarball() {
    local url=$1
    local symlinktarget=$2

    local tarballname=$(echo "${url}" | rev | cut -d'/' -f1 | rev)
    local symlinkname=$(echo "${symlinktarget}" | rev | cut -d'/' -f1 | rev)

    echo "Installing ${url} to ${symlinktarget}..."

    mkdir -p /tmp/ballinstall /opt/${symlinkname}
    curl -sSL -o "/tmp/ballinstall/${tarballname}" "${url}"
    tar xf "/tmp/ballinstall/${tarballname}" -C "/opt/${symlinkname}"
    ln -s "${symlinktarget}" /usr/local/bin/${symlinkname}
    rm -rf /tmp/ballinstall
}

install_from_github() {
    local owner=$1
    local repo=$2
    local release_asset_format=$3
    local symlink_target=$4
    local version=${5-"latest"}

    local asset_url=$(find_github_release_asset_url ${owner} ${repo} ${release_asset_format} ${version})

    download_and_install_gzipped_tarball "${asset_url}" "${symlink_target}"
}

export -f install_from_github