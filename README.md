## Тестовое задание для "Практика"

### Запуск проекта:

```console
docker-compose --env-file src/config/.env up -d
docker-compose --env-file src/config/.env exec app bash
./manage.py migrate
./manage.py createsuperuser
```
