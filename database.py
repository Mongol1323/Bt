import sqlite3

# Имя файла базы данных
DB_NAME = "expenses.db"

def get_connection():
    """Подключение к базе данных SQLite."""
    conn = sqlite3.connect(DB_NAME)
    # Позволяет обращаться к колонкам по имени (например, row['amount'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Читает schema.sql и создает таблицы в базе."""
    with get_connection() as conn:
        with open("schema.sql", "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    print("База данных успешно инициализирована!")

def add_expense(amount, category, description=""):
    """Добавить новую трату в базу данных."""
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
            (amount, category, description)
        )
        # conn.commit() — это сохранение изменений в базе данных (без него данные стерутся при закрытии)
        conn.commit()
    print("Трата успешно добавлена!")

def get_all_expenses():
    """Забрать все траты из базы данных."""
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM expenses")
        # cursor.fetchall() — это метод, который забирает все найденные строки в виде списка
        return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    add_expense(777.00, "Продукты", "Транспорт")

    print("\nСписок всех трат:")
    for row in get_all_expense():
        print(f"ID: {row['id']} | Сумма: {row['amount']} | Категория: {row['category']} | Описание: {row['description']}")