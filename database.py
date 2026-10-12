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
def delete_expense(expense_id):
    """Удалить трату из базы по её ID."""
    with get_connection() as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
    print(f"Трата с ID {expense_id} успешно удалена!")

def get_all_expenses():
    """Забрать все траты из базы данных."""
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM expenses")
        # cursor.fetchall() — это метод, который забирает все найденные строки в виде списка
        return cursor.fetchall()

if __name__ == "__main__":
    init_db()

    while True:
        print("\n=== ТРЕКЕР РАСХОДОВ ===")
        print("1. Добавить новую трату")
        print("2. Посмотреть все траты")
        print("3. Удалить трату по ID")
        print("4. Выход")
        choice = input("Выбери пункт: ")

        if choice == "1":
            # Спрос суммы с защитой от ввода букв
            while True:
                amount_str = input("Введи сумму: ")
                try:
                    ammount = float(amount_str)
                    if ammount <= 0:
                        print("Сумма должна быть больше нуля, не тупи.")
                        continue
                    break
                except ValueError:
                    print("Бл*, это не число! Напиши цифрами, а не буквами.")
            category = input("Введи категорию (Продукты, транспорт, заказы, ежемесячные траты): ")
            description = input("Описание: ")

            add_expense(ammount, category, description)

        elif choice == "2":
            print("\n--- ТВОИ ТРАТЫ БАЛЯ ---")
            expenses = get_all_expenses()
            if not expenses:
                print("База пустая, потрать что нибудь сначала")
            else:
                for row in expenses:
                    print(f"ID: {row['id']} | Сумма: {row['amount']} | Категория: {row['category']} | Описание: {row['description']}")

        elif choice == "3":
            # Срашиваем ID для удаление
            expenses_id_str = input("Введи ID траты, которую нужно удалить: ")
            try:
                expense_id = int(expenses_id_str)
                delete_expense(expense_id)
            except ValueError:
                print("ID Должен быть ЦЕЛЫМ числом")
        elif choice == "4":
            print("Давай... Чекалды Пока!)")
            break
        else:
            print("Чел, выбери одно из Четырех, ЧЕУ")
