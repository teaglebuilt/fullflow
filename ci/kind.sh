#!/usr/bin/env bash

set -e

setup_network() {
  # Calico
  curl https://docs.projectcalico.org/manifests/calico.yaml | kubectl apply -f -

  # CoreDNS
  kubectl scale deployment --replicas 1 coredns --namespace kube-system
}

setup_metrics() {
  # Metrics Server
  helm repo add stable https://kubernetes-charts.storage.googleapis.com
  helm repo update
  helm upgrade metrics-server --install --set "args={--kubelet-insecure-tls, --kubelet-preferred-address-types=InternalIP}" stable/metrics-server --namespace kube-system
}

kind create cluster \
  --config local-cluster.yaml \
  --name fullflow


if [ "$1" == "ingress" ]
  then
    setup_network
fi

setup_metrics