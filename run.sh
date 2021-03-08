#!/usr/bin/env bash
set -euo pipefail



open() {
    echo "port forwarding ${1} over ${2}"
    kubectl port-forward "${1}" "${2}"
}

upgrade() {
    echo "uprading helm chart"
    helm upgrade fullflow chart/ --debug
}

install() {
    echo "Installing Fullflow helm chart"
    helm install fullflow chart/
}

build-docker() {
    echo "build and push docker image for environment"
    docker build --tag teaglebuilt/fullflow:${1} .
    docker push teaglebuilt/fullflow:${1}
}

build-static() {
    jlpm install
    jlpm build
}

function extension {
    pip install -e .
    jupyter serverextension enable --py fullflow --sys-prefix
    jupyter nbextension install --py fullflow --sys-prefix
    jupyter nbextension enable --py fullflow --sys-prefix
}

function help {
    printf "%s <task> [args]\n\nTasks:\n" "${0}"
    compgen -A function | grep -v "^_" | cat -n
    printf "\nExtended help:\n "
}


"${@:-help}"
