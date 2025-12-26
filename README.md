# Scrapy PEP - Асинхронный парсер документов PEP на базе фреймворка Scrapy.

[![Python](https://img.shields.io/badge/-Python-3771a1?style=flat&logo=Python&logoColor=ffffff)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-15b8a6?style=flat&logo=Scrapy&logoColor=ffffff)](https://scrapy.org/)

Автор - [Халин Вадим](https://t.me/gohub1)

---

## Оглавление:
- [Описание](#описание)
- [Основные технологии](#основные-технологии)
- [Запуск проекта](#запуск-проекта)

---

## Описание:
Парсер документов PEP (Python Enhancement Proposals) с сайта [PEP](https://peps.python.org) на базе фреймворка Scrapy.
В результате выполнения будут созданы два файла формата (**csv**) в папке results:

1. pep_{time_now} - Список всех PEP (Номер, Название, Статус).
2. status_summary_{time_now} - Сводка по статусам (Подсчет каждого статуса и общее количество) из первого файла.

---

## Основные технологии:
- Python
- Scrapy

---

## Запуск проекта:
1. Клонируем репозиторий.
```
git clone https://github.com/GohubSilently/scrapy_parser_pep
cd scrapy_parser_pep
```

2. Создаем виртуальное окружение и активируем его.
```
python3 -m venv .venv && source .venv/bin/activate
```

3. Установка зависимостей проекта.
```
pip install --upgrade pip && pip install -r requirements.txt
```

4. Запускаем парсер.
```
scrapy crawl pep
```
