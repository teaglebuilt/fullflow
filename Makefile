CHARTS = jupyterhub
env := dev


.PHONY: uninstall install
install:
	helm install fullflow chart/

uninstall:
  helm uninstall fullflow


.PHONY: build
build:
  @docker build --tag teaglebuilt/fullflow:$(env) .

forward:
  kubectl port-forward svc/fullflow-webserver 8080:8080

.PHONY: notebook
notebook:
  jupyter notebook --gateway-url=0.0.0.0:9000 --GatewayClient.auth_token='poop' --GatewayClient.request_timeout=600