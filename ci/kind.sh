#!/usr/bin/env bash
set -e

setup_network() {
  # Cluster
  kind create cluster \
    --config ci/local-cluster-net.yaml \
    --name fullflow

  # Calico
  curl https://docs.projectcalico.org/manifests/calico.yaml | kubectl apply -f -

  # CoreDNS
  kubectl scale deployment --replicas 1 coredns --namespace kube-system
}

setup_loadbalancer() {
  kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)"
  docker network inspect -f '{{.IPAM.Config}}' kind
  for _ in {1..10}; do
    curl ${LB_IP}:5678
  done
}

setup_metrics() {
  # Metrics Server
  helm repo add stable https://kubernetes-charts.storage.googleapis.com
  helm repo update
  helm upgrade metrics-server --install --set "args={--kubelet-insecure-tls, --kubelet-preferred-address-types=InternalIP}" stable/metrics-server --namespace kube-system
}


if [ "$1" == "ingress" ]
  then
    setup_network
  else
    kind create cluster \
      --config ci/local-cluster.yaml \
      --name fullflow
fi

setup_metrics
