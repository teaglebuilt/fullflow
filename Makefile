

build:
	docker build --tag teaglebuilt/airflow:dev .

push:
	docker push teaglebuilt/airflow:dev

ilocal:
	helm install fulllow chart/ --values=chart/environments/local.yaml