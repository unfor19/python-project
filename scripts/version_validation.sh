#!/bin/bash
_RELEASE_VERSION=${RELEASE_VERSION:-$1}
_VERBOSE=${VERSION_VALIDATION_VERBOSE:-"true"}

msg_error(){
    local msg="$1"
    echo -e ">> [ERROR] $msg"
    exit 1
}

msg_log(){
    local msg="$1"
    if [[ $_VERBOSE = "true" ]]; then
        echo -e ">> [LOG] $msg"
    fi
}

if [[ $_RELEASE_VERSION =~ ^[0-9]{1,}(\.[0-9]*)*(\.(a|b|rc)[0-9]{1,}|(\.post[0-9]{1,})|(\.dev[0-9]{1,})){0,1}$ ]]; then
    msg_log "Passed - Release version is valid"
    echo "$_RELEASE_VERSION"
else
    msg_log "Failed - Release version is invalid"
    echo ""
fi