# Комплект проекта

В архиве сохранены обе версии приложения, редактор и подготовленные Excel.

| Папка | Содержимое |
| --- | --- |
| `Shop_Desktop` | Цельная версия магазина, импорт, редактор и аналитика |
| `Shop_Modules` | Те же этапы задания в пяти самостоятельных модулях |
| `Excel_Data` | Исходная подготовленная выгрузка с профилем импорта |

## Запуск

Выбери одну версию и открой терминал в её папке.

Mac / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Заполни `postgres_connection.json`, запусти PostgreSQL и затем:

```bash
python import_db.py
python main.py
```

В импортёре выбери XLSX из `Excel_Data`. Соответствующий
`import_profile.json` должен оставаться рядом с ними.

Редактор запускается отдельно:

```bash
python Excel_Tool/main.py
```

Если Tkinter не установлен, порядок установки для своей системы смотри
в `INSTRUCTION.md` выбранной версии.

## Что где менять

| Файл или папка | Назначение |
| --- | --- |
| `config.py` | Возможности приложения, таблицы, поля и справочники |
| `design.py` | Цвета, размеры, подписи и вид карточек |
| `postgres_connection.json` | Подключение к обычному PostgreSQL или Docker |
| `ui/screens/` | Главное окно, каталог, вход, заказы и настройка данных |
| `ui/components/` | Карточка товара |
| `ui/widgets.py` | Общие элементы интерфейса |
| `data_access/database.py` | Чтение и запись PostgreSQL |
| `data_access/orders.py` | Заказы, скидки и остатки |
| `data_access/mapping.py` | Сопоставление структуры и чтение справочников |
| `excel_io/` | Разбор Excel и импорт в PostgreSQL |
| `maintenance/` | Проверка подключения и структуры |
| `images/` | Фото товаров |
| `assets/` | Логотип и служебные изображения |
| `Excel_Tool/` | Независимый редактор Excel |
| `Statistics/` | Аналитика в цельной версии |

В модульной версии настройки магазина и папки `ui`, `data_access`,
`images` находятся внутри соответствующего модуля. Полный магазин —
`Module_4_Orders`, импорт — `Module_1_Database`, аналитика —
`Module_5_Analytics`. Корневые `main.py` и `import_db.py` запускают их.

Команды запуска сохранены. Перенесены файлы и обновлены импорты; изменена
палитра. Данные, SQL, настройки подключения и прикладная логика сохранены.
Подробная инструкция находится в `INSTRUCTION.md` выбранной версии.
