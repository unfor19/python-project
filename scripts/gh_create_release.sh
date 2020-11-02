#!/bin/bash

### Requirements
# 1. GitHub CLI - https://cli.github.com/
# 2a. Generate GitHub Personal Access Token - https://github.com/settings/tokens
# 2b. Scope: repo(all), admin:org(read:org), admin:public_key(read:public_key)

### Usage
# bash scripts/gh_create_release.sh ${GITHUB_OWNER} ${GITHUB_REPOSITORY} ${RELEASE_VERSION}
###

set -e
_GITHUB_OWNER=${GITHUB_OWNER:-$1}
_GITHUB_REPOSITORY=${GITHUB_REPOSITORY:-$2}
_RELEASE_VERSION=${RELEASE_VERSION:-$3}


msg_error(){
    local msg="$1"
    local exit_code=${2:-1}
    echo -e ">> [ERROR]: $msg"
    exit "$exit_code"
}


# Arguments validation
if [[ -z $_GITHUB_OWNER || -z $_GITHUB_REPOSITORY || -z $_RELEASE_VERSION ]]; then
    msg_error "Missing argument(s)\nGITHUB_OWNER = ${_GITHUB_OWNER}\nGITHUB_REPOSITORY = ${_GITHUB_REPOSITORY}\nRELEASE_VERSION = ${_RELEASE_VERSION}"
fi


# Authenticate with GitHub
gh config set prompt disabled
gh auth login --with-token < .gh_token


# Create release in GitHub
set +e
read -r _EXIT_MSG < <(gh release create "$_RELEASE_VERSION" -t "$_RELEASE_VERSION" -R "${_GITHUB_OWNER}/${_GITHUB_REPOSITORY}")
_EXIT_CODE=$?
gh config set prompt enabled
if [[ $_EXIT_CODE -ne 0 ]]; then
    [[ -z $_EXIT_MSG ]] && _EXIT_MSG="Error log above"
    msg_error "$_EXIT_MSG" "$_EXIT_CODE"
fi
