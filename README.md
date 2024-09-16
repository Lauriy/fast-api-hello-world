Get a venv and activate, then:
```shell
pip install uv
uv sync
fastapi dev main.py
```

Quality:
```shell
pre-commit install
pre-commit run --all-files
```

Migrations:
```shell
alembic revision --autogenerate -m "create users & items"
alembic upgrade head
```
