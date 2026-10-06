import random

templars = [
    {"name": "Helbrecht", "rank": "High Marshal", "power": 150, "kills": 4300, "unit": "Command"},
    {"name": "Grimaldus", "rank": "High Chaplain", "power": 120, "kills": 2800, "unit": "Command"},
    {"name": "Brother Bayard", "rank": "Emperor's Champion", "power": 110, "kills": 1900, "unit": "Elites"},
    {"name": "Brother Tannhauser", "rank": "Sword Brother", "power": 110, "kills": 2400, "unit": "Elites"},
]

# Варианты званий для элиты 1-й роты
ranks = ["Sword Brother", "Terminator Vet", "Vanguard Vet", "Sternguard Vet"]
units = ["1st Company", "Terminator Squad", "Sword Brethren"]

# Добиваем массив до 100 десантников
random.seed(42)  # Зафиксируем генератор, чтобы числа не прыгали при каждом запуске
for i in range(1, 97):
    templars.append({
        "name": f"Brother {i}",
        "rank": random.choice(ranks),
        "power": random.randint(50, 130),
        "kills": random.randint(300, 3500),
        "unit": random.choice(units)
    })


# функции сортировки

def quicksort_multi(units):
    if len(units) <= 1:
        return units
    pivot = units[len(units) // 2]
    p_tuple = (pivot["power"], pivot["kills"])

    left = [x for x in units if (x["power"], x["kills"]) < p_tuple]
    middle = [x for x in units if (x["power"], x["kills"]) == p_tuple]
    right = [x for x in units if (x["power"], x["kills"]) > p_tuple]

    return quicksort_multi(left) + middle + quicksort_multi(right)
# вывод таблицы

def print_table(units, limit=15):
    # Выводим первые `limit` бойцов, чтобы не засирать весь терминал 100 строками
    print(f"{'NAME':<22} | {'RANK':<16} | {'POWER':<8} | {'KILLS':<8}")
    print("-" * 62)
    for unit in units[:limit]:
        print(f"{unit['name']:<22} | {unit['rank']:<16} | {unit['power']:<8} | {unit['kills']:<8}")
    if len(units) > limit:
        print(f"... и еще {len(units) - limit} ветеранов роты ...")
# бинарный поиск
def binary_search_multi(units, target_tuple):
    left = 0
    right = len(units) - 1
    while left <= right:
        mid = (left + right) // 2
        current_tuple = (units[mid]["power"], units[mid]["kills"])
        if current_tuple == target_tuple:
            return units[mid]
        elif current_tuple < target_tuple:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Сортируем все 100 бойцов
sorted_1st_company = quicksort_multi(templars)

print(f"Всего в 1-й роте: {len(sorted_1st_company)} космодесантников.\n")

# Печатаем топ-15 самых слабых/сильных по power и kills
print_table(sorted_1st_company, limit=101)


def find_boarding_pair(units, target_power):
    left = 0
    right = len(units) - 1
    while left < right:
        current_sum = units[left]["power"] + units[right]["power"]

        if current_sum == target_power:
            return (units[left], units[right])
        elif current_sum < target_power:
            left += 1
        else:
            right -= 1
    return None

# --- ТЕСТИРУЕМ ДВА УКАЗАТЕЛЯ ---

target = 200  # Ищем двух бойцов с суммарной силой ровно 200
pair = find_boarding_pair(sorted_1st_company, target)

if pair:
    marine1, marine2 = pair
    print(f"\n[!] Абордажная пара под силу {target} найдена:")
    print(f"1. {marine1['rank']} {marine1['name']} (Power: {marine1['power']})")
    print(f"2. {marine2['rank']} {marine2['name']} (Power: {marine2['power']})")
    print(f"Проверка суммы: {marine1['power']} + {marine2['power']} = {marine1['power'] + marine2['power']}")
else:
    print(f"\n[-] Нельзя собрать пару с суммарной силой {target}.")