# Иерархическое дерево Крестового Похода
crusade_tree = {
    "name": "Helbrecht", "rank": "High Marshal", "power": 150,
    "subordinates": [
        {
            "name": "Castellan Draco", "rank": "Castellan", "power": 95,
            "subordinates": [
                {"name": "Brother Tannhauser", "rank": "Sword Brother", "power": 110, "subordinates": []},
                {"name": "Initiate Vane", "rank": "Initiate", "power": 45, "subordinates": []}
            ]
        },
        {
            "name": "Grimaldus", "rank": "High Chaplain", "power": 120,
            "subordinates": [
                {"name": "Brother Bayard", "rank": "Emperor's Champion", "power": 110, "subordinates": []},
                {"name": "Neophyte Toby", "rank": "Neophyte", "power": 15, "subordinates": []}
            ]
        }
    ]
}


# Рекурсивный поиск в глубину (DFS)
def calculate_total_power(commander):
    # Base Case / Текущее значение: сила самого командира
    total_power = commander["power"]

    # Recursive Step / Рекурсивный шаг: считаем силу каждого подчиненного
    for sub in commander["subordinates"]:
        total_power += calculate_total_power(sub)  # Функция вызывает сама себя!

    return total_power


# --- ПРОВЕРКА ---

# 1. Считаем силу всей группировки Хелбрехта
full_power = calculate_total_power(crusade_tree)
print(f"Общая сила всего Крестового Похода Хелбрехта: {full_power}")

# 2. Считаем силу только отряда Кастеляна Драко (без Хелбрехта и Гримальдуса)
draco_branch = crusade_tree["subordinates"][0]
draco_power = calculate_total_power(draco_branch)
print(f"Сила отряда Кастеляна Драко: {draco_power}")


def print_tree(commander, level=0):
    # Умножаем пробелы на уровень, чтобы сдвинуть текст вправо
    indent = "    " * level

    # Добавляем красивую веточку, если это не Маршал (level > 0)
    branch = "└── " if level > 0 else ""

    # Печатаем текущего десантника
    print(f"{indent}{branch}[{commander['rank']}] {commander['name']} (Power: {commander['power']})")

    # Рекурсивный шаг: перебираем подчиненных и вызываем эту же функцию, но level + 1
    for sub in commander["subordinates"]:
        print_tree(sub, level + 1)


# --- ВЫЗОВ ФУНКЦИИ ---
print("\nИерархия Крестового Похода:")
print_tree(crusade_tree)