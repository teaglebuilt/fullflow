#!/usr/bin/env bash
set -euo pipefail

local() {
    echo "Running Locally"
    honcho -f Procfile start
}

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

uninstall() {
    helm uninstall fullflow
}

build-docker() {
    echo "build and push docker image for environment"
    docker build --tag teaglebuilt/fullflow:${1} .
    docker push teaglebuilt/fullflow:${1}
}


kernels() {
    http GET $JUPYTER_GATEWAY_URL/api/kernels
}

clean() {
    rm -rf .pytest_cache/ .coverage dist build *.egg-info
    find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
    rm .coverage coverage.xml
    rm logs
}

package() {
    clean
    python setup.py sdist bdist_wheel
}

ci() {
    flux bootstrap github \
        --owner=teaglebuilt \
        --repository=fullflow \
        --branch=master \
        --path=./chart \
        --personal
}

cluster() {
    echo "creating local cluster"
    ./ci/kind.sh
}


export() {
    if [ -z "$1" ]
      then
        echo "exporting parent chart"
        helm template . --output-dir './export'
    else
        echo "exporting chart $1 into export/$1"
        helm template ./chart/charts/$1 --output-dir './export'
    fi
}

watch() {
  case $input in
    lb)
      echo "watching LB"
      kubectl get pods -n metallb-system --watch ;;
    *)
      echo "Watch yourself instead.." ;;
  esac
}


function help {
  printf "%s <task> [args]\n\nTasks:\n" "${0}"
  compgen -A function | grep -v "^_" | cat -n
  printf "\nExtended help:\n "
}


"${@:-help}"
