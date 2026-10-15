from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data_access.database import Database

if __name__ == "__main__":
    database = Database()
    print("Подключение к PostgreSQL успешно. Таблицы доступны.")
    database.close()
