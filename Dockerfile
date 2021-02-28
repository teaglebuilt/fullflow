FROM python:3.8-slim-buster

SHELL ["/bin/bash", "-l", "-c"]

# Airflow
ARG AIRFLOW_VERSION=2.0.0
ARG AIRFLOW_USER=airflow
ARG AIRFLOW_USER_HOME=/usr/local/airflow
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.8.txt"

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

RUN mkdir -p ${AIRFLOW_HOME}
WORKDIR ${AIRFLOW_HOME}

# User Add & Super User setting & apt library install
RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} -G sudo ${AIRFLOW_USER} && \
    apt-get install -y --fix-broken && \
    apt-get autoremove && \
    apt-get update && apt-get -y upgrade && \
    apt-get install -y --no-install-recommends apt-utils \
    freetds-bin \
    ldap-utils \
    libffi6 \
    libsasl2-2 \
    libsasl2-modules \
    libssl1.1 \
    locales  \
    lsb-release \
    sasl2-bin \
    sqlite3 \
    unixodbc \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    build-essential \
    net-tools iputils-ping

# COPY local airflow directory
COPY dags ${AIRFLOW_HOME}/dags
COPY src ${AIRFLOW_HOME}/src
COPY k8s ${AIRFLOW_HOME}/k8s
COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt ${AIRFLOW_HOME}/requirements.txt

RUN pip install -r requirements.txt

RUN chown -R ${AIRFLOW_USER}:${AIRFLOW_USER} ${AIRFLOW_USER_HOME}
RUN chmod +x /entrypoint.sh

EXPOSE 8080 5555 8793

USER ${AIRFLOW_USER}
WORKDIR ${AIRFLOW_USER_HOME}
ENTRYPOINT ["/entrypoint.sh"]