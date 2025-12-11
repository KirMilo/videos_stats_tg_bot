## Telegram-бот для аналитики по видео на основе задач на естественном языке.

### Стек:
- python 3.13
- aiogram
- openai
- sqlalchemy
- pydantic
- alembic
- asyncio
- uv
- docker/docker-compose

### Структура проекта
```
├── src
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── db
│   │       ├── __init__.py
│   │       ├── models
│   │       │   ├── __init__.py
│   │       │   ├── base.py
│   │       │   ├── video_snapshots.py
│   │       │   └── videos.py
│   │       └── session.py
│   ├── llm
│   │   ├── __init__.py
│   │   ├── prompt.py
│   │   └── service.py
│   └── main.py
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 1f9859e3d6cd_initial.py
│       └── 2457a0eb8a9a_filling_data.py
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── pyproject.toml
├── README.md
├── .env.example
```

### Быстрый запуск:
1. `https://github.com/KirMilo/videos_stats_tg_bot`
2. Создать файл `.env.prod` в корне проекта и заполнить по примеру `.env.example`
3. `docker compose up -d`

- Миграции накатятся автоматически при запуске.
