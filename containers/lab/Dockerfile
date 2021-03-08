FROM jupyter/minimal-notebook

USER root

COPY fullflow.whl /tmp

RUN apt-get update && apt-get install -y curl

RUN pip install --upgrade pip && \
    pip install setuptools --ignore-installed --upgrade && \
    pip install --upgrade jupyter_contrib_nbextensions jupyterlab fullflow /tmp/fullflow*.whl && \
    jupyter contrib nbextension install --sys-prefix && \
	jupyter serverextension enable --py fullflow --sys-prefix && \
	jupyter nbextension install --py fullflow --sys-prefix && \
	jupyter nbextension enable --py fullflow --sys-prefix && \
	rm -f /tmp/fullflow*.whl

ADD entrypoint.sh /usr/local/share/jupyter/

ENTRYPOINT ["/usr/local/share/jupyter/entrypoint.sh"]
CMD ["lab"]

USER jovyan

WORKDIR /home/jovyan/work