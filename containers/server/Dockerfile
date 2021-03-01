
FROM julitopower/python36emacs25elpy

ADD requirements.txt /opt/server/requirements.txt
WORKDIR /opt/server
RUN python -m pip install -r requirements.txt

# Install nodejs 10.x
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN apt-get install -y nodejs

RUN jupyter serverextension enable --py nb2kg --sys-prefix && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager


WORKDIR /opt/src
CMD ["jupyter", "notebook", \
     "--NotebookApp.ip=0.0.0.0", \
     "--NotebookApp.session_manager_class=nb2kg.managers.SessionManager", \
     "--NotebookApp.kernel_manager_class=nb2kg.managers.RemoteKernelManager", \
     "--NotebookApp.kernel_spec_manager_class=nb2kg.managers.RemoteKernelSpecManager"]