#!/usr/bin/env bash
set -euo pipefail


upgrade() {
    echo "uprading helm chart"
    helm upgrade fullflow chart/ --debug
}

install() {
    echo "Installing Fullflow helm chart"
    helm install fullflow chart/
}

function help {
    printf "%s <task> [args]\n\nTasks:\n" "${0}"
    compgen -A function | grep -v "^_" | cat -n
    printf "\nExtended help:\n "
}


"${@:-help}"