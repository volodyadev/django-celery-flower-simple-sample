# Запуск проекта

Для запуска проекта используйте следующую команду:

```bash
docker-compose up --build
```

# Создание задачи

```bash
curl -X POST -d "value=30" http://127.0.0.1:1337/tasks/
```

# Отслeживаем задачи

http://localhost:5555/tasks