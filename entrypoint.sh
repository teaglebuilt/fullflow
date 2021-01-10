#!/bin/sh
CMD_AIRFLOW_COMMAND_PASSED="$1"

if [ -e ".env" ]; then
    set -a
    . .env
    set +a
fi

echo $PYTHONPATH

case "$1" in
webserver)
    # Give the scheduler time to run initdb.
    sleep 20
    if [ "$AIRFLOW__CORE__EXECUTOR" = "LocalExecutor" ] || [ "$AIRFLOW__CORE__EXECUTOR" = "SequentialExecutor" ]; then
        # With the "Local" and "Sequential" executors it should all run in one container.
        airflow scheduler &
    fi
    echo "Starting Web Server"
    airflow webserver
    ;;
scheduler)
    echo "Initializing DB"
    airflow db init
    if [ "$WORKFLOW_UPGRADE_DB" = "True" ]; then
        echo "Upgrading DB"
        airflow db upgrade
    fi
    echo "Creating Admin User"
    airflow users create --role Admin --username admin --email bandikishores@gmail.com --firstname Workflow --lastname Service --password admin
    echo "Starting Scheduler"
    exec airflow "$@"
    ;;
worker)
    # Give the scheduler time to run initdb.
    sleep 20
    echo "Starting Worker"
    exec airflow "$@"
    ;;
version)
    echo "Printing Version"
    exec airflow "$@"
    ;;
bash)
    echo "Executing Bash"
    exec "/bin/bash" "$@"
    ;;
python)
    echo "Executing Python"
    exec "python" "$@"
    ;;
*)
    # The command is something like bash, not an airflow subcommand. Just run it in the right environment.
    echo "Executing Command Sent"
    exec "$@"
    ;;
esac
