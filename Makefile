CHARTS = jupyterhub
env := dev


.PHONY: install
install:
	helm install fullflow chart/

.PHONY: build
build:
  @docker build --tag teaglebuilt/fullflow:$(env) .

forward:
  kubectl port-forward svc/fullflow-webserver 8080:8080
gateway:
  jupyter kernelgateway --KernelGatewayApp.ip=0.0.0.0 --KernelGatewayApp.port=8888