#!/bin/sh

repo_name=$(basename "$PWD")

docker-compose rm -sf jupyter greenplum zookeeper kafka producer consumer airflow
docker volume rm "${repo_name}_db"
