# Тестирование линтеров ruff и black

Этот проект демонстрирует, как использовать линтеры ruff и black в Python проектах, а также включает тесты для проверки их работы.

## Установка

Для установки зависимостей проекта выполните:

```bash
pip install -r requirements.txt
```

## Структура проекта

- `main.py` - пример файла с кодом, который содержит стилистические ошибки
- `test_linters.py` - тесты для проверки работы линтеров ruff и black
- `pyproject.toml` - файл конфигурации для линтеров
- `requirements.txt` - файл с зависимостями

## Запуск тестов

Для запуска тестов выполните:

```bash
python test_linters.py
```

или с помощью pytest:

```bash
pytest test_linters.py -v
```

## Запуск линтеров вручную

### Проверка кода с помощью ruff

```bash
ruff check main.py
```

### Исправление ошибок с помощью ruff

```bash
ruff --fix main.py
```

### Проверка форматирования с помощью black

```bash
black --check main.py
```

### Форматирование с помощью black

```bash
black main.py
```

## Настройка pre-commit hook

Вы можете настроить pre-commit hook для автоматического запуска линтеров перед каждым коммитом. Для этого создайте файл `.pre-commit-config.yaml` с следующим содержанием:

```yaml
repos:
-   repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.1
    hooks:
    -   id: ruff
        args: [--fix, --exit-non-zero-on-fix]
-   repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
    -   id: black
```

Затем установите pre-commit и настройте hook:

```bash
pip install pre-commit
pre-commit install
``` 
