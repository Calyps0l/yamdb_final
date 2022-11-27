https://github.com/Calyps0l/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg

## Описание
Проект по работе с Docker-compose

### Запускаем проект:
клонируем репозиторий

```bash
git clone https://github.com/Calyps0l/yamdb_final
```
переходим в него
```bash
cd api_yamdb
```

создаем виртуальное окружение
```bash
python -m venv venv
venv/scripts/activate
```

устанавливаем зависимости
```bash
pip install -r requurements.txt
```

переходим в infra и собираем контейнеры
```bash
cd infra
docker-compose up -d --build
```

выполняем миграции
```bash
docker-compose exec web python manage.py migrate
```

создаем суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

собираем статику
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

заполняем бд
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

по окончанию работы останавливаем контейнеры
```bash
docker-compose down -v
```

### Запросы:
Примеры запросов находятся по адресу: http://localhost:8000/redoc/

### Шаблон по заполнению .env (infra/.env)
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```