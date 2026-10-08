# ShopStream at Scale — Distributed Batch Analytics with PySpark

Batch-слой на Apache Spark для синтетического e-commerce clickstream (~2.8M событий):
сырые JSON → очистка и контроль качества → silver-таблица в Parquet → аналитика
(воронка, сессии, топ-товары, DAU/WAU) → исследование joins/skew/AQE и бенчмарки.

> Учебный проект (Big Data course, Astana IT University). Описание результатов — в `report/report.pdf`.

## Структура

```
├── ibaidullina.ipynb   # весь код и объяснения, по частям A–F
├── run_a2.py           # воспроизводит всё одной командой
├── requirements.txt
├── results/            # CSV и PNG, которые создаёт ноутбук
└── report/             # report.pdf
```

## Как запустить

Требования: Python 3.11, Java 17. На Windows также нужен winutils (см. ниже).

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Данные создаются генератором курса `shopstream_gen.py` (не входит в репозиторий),
его нужно положить в корень проекта. Затем:

```bash
python run_a2.py --scale medium --seed <SEED>
```

### Windows: winutils
Положите `winutils.exe` и `hadoop.dll` (Hadoop 3.3.x) в `C:\hadoop\bin`.
Ноутбук сам выставит `HADOOP_HOME=C:\hadoop`.

## Окружение
Заполняется автоматически в `results/environment.json`.
