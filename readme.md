# Запуск

## Prerequisites

Ставим poetry: https://pypi.org/project/poetry/

## Старт сервера

Устанавливаем зависимости:
```bash
make setup
```

Сначала запускаем базу:
```bash
make db
```

Затем Django:
```bash
make run
```