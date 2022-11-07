# Разделы проекта

1. airflow - содержит конфигурацию Docker-контейнера Airflow
2. greenplum - содержит конфигурацию Docker-контейнера Greenplum
3. dags - содержит DAG-файлы для Airflow
4. producer - содержит producer для Kafka
5. consumer - содержит consumer для Kafka
5. venv.ps1/venv.sh - загрузка зависимостей для windows/linux соответственно
6. ps.sh - мониторинг состояния контейнеров (Linux)

# Запуск

Необходимо ввести команду в корне репозитория:
`docker-compose up`

# Системные требования

Требуется:
* 8ГБ RAM и более
* 6ГБ дискового пространства

Протестирована работа на ПО:
* Docker версии 20.10.18
* Docker-Compose версии 1.29.2
