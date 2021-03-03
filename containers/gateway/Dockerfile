FROM jupyter/datascience-notebook:latest

# install the kernel gateway
RUN pip install --no-cache-dir jupyter_kernel_gateway

# run kernel gateway on container start, not notebook server
EXPOSE 8888
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888", "--JupyterWebsocketPersonality.list_kernels=True"]