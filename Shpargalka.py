# ==============================================================================
# 1. ПЕРЕМЕННЫЕ И ТИПЫ ДАННЫХ (Variables & Data Types)
# ==============================================================================

# Строки (str)
first_name = "Alex"
food = "pizza"

# Целые числа (int)
age = 20
quantity = 3

# Числа с плавающей точкой (float)
price = 10.99
gpa = 3.8

# Логический тип (bool)
is_student = True
for_sale = False

# Вывод с использованием f-строк (f-strings)
print(f"Привет, {first_name}! Тебе {age} лет.")
print(f"Итоговая цена: ${price * quantity}")


# ==============================================================================
# 2. ПРИВЕДЕНИЕ ТИПОВ (Typecasting)
# ==============================================================================

name = "Code"
age = 20
gpa = 3.5
is_student = True

# Явное приведение типов
gpa = int(gpa)          # 3.5 -> 3
age = float(age)        # 20 -> 20.0
age_str = str(age)      # 20.0 -> "20.0"
name_bool = bool(name)  # Пустая строка -> False, непустая -> True


# ==============================================================================
# 3. ВВОД ДАННЫХ (User Input)
# ==============================================================================

# input() всегда возвращает строку (str)!
# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: ")) # Сразу приводим к int


# ==============================================================================
# 4. МАТЕМАТИКА И ВСТРОЕННЫЕ ФУНКЦИИ (Math Operations)
# ==============================================================================

import math

x = 3.14
y = -4
z = 5

# Встроенные функции
result_round = round(x)     # Округление (3)
result_abs = abs(y)         # Абсолютное значение (4)
result_pow = pow(4, 3)      # Возведение в степень (4^3 = 64)
result_max = max(x, y, z)   # Максимум (5)
result_min = min(x, y, z)   # Минимум (-4)

# Модуль math
math_sqrt = math.sqrt(16)   # Квадратный корень (4.0)
math_ceil = math.ceil(x)    # Округление вверх (4)
math_floor = math.floor(x)  # Округление вниз (3)
pi_value = math.pi          # Константа Pi (~3.14159)


# ==============================================================================
# 5. УСЛОВНЫЕ ОПЕРАТОРЫ И ЛОГИКА (If / Elif / Else & Logical Operators)
# ==============================================================================

age = 18
has_ticket = True

# Логические операторы: and, or, not
if age >= 18 and has_ticket:
    print("Вход разрешен")
elif age < 18 or not has_ticket:
    print("Вход воспрещен")
else:
    print("Проверьте документы")

# Тернарный оператор (Ternary Operator)
status = "Взрослый" if age >= 18 else "Несовершеннолетний"


# ==============================================================================
# 6. РАБОТА СО СТРОКАМИ И СРЕЗЫ (Strings & Slicing)
# ==============================================================================

text = "Python Programming"

# Методы строк
length = len(text)                   # Длина строки
find_idx = text.find("o")            # Поиск первого вхождения (индекс)
rfind_idx = text.rfind("o")          # Поиск последнего вхождения
upper_text = text.upper()            # В верхний регистр
lower_text = text.lower()            # В нижний регистр
is_num = text.isdigit()              # Проверка: состоит ли только из цифр
is_alpha = text.isalpha()            # Проверка: состоит ли только из букв
count_o = text.count("o")            # Подсчет символов
replaced = text.replace("o", "a")    # Замена символов

# Срезы: [start : stop : step]
phrase = "123456789"
first_three = phrase[:3]             # "123"
middle = phrase[3:6]                 # "456"
reversed_str = phrase[::-1]          # "987654321" (разворот строки)


# ==============================================================================
# 7. ЦИКЛЫ (While, For, Range)
# ==============================================================================

# Цикл While
counter = 1
while counter <= 3:
    print(f"Шаг {counter}")
    counter += 1

# Цикл For и range(start, stop, step)
for i in range(1, 6, 2):             # Выведет: 1, 3, 5
    print(i)

# Операторы управления циклом: break, continue, pass
for i in range(1, 10):
    if i == 3:
        continue                     # Пропустить итерацию
    if i == 6:
        break                        # Прервать цикл полностью


# ==============================================================================
# 8. КОЛЛЕКЦИИ (Lists, Sets, Tuples, Dictionaries)
# ==============================================================================

# --- СПИСКИ / LISTS (упорядоченные, изменяемые, допускают дубликаты) ---
fruits = ["apple", "orange", "banana"]
fruits.append("coconut")             # Добавить в конец
fruits.insert(0, "pineapple")        # Вставить по индексу
fruits.remove("orange")              # Удалить по значению
popped = fruits.pop()                # Извлечь последний элемент
fruits.sort()                        # Сортировка по возрастанию
fruits.reverse()                     # Разворот списка

# --- МНОЖЕСТВА / SETS (неупорядоченные, уникальные элементы) ---
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.remove("red")

# --- КОРТЕЖИ / TUPLES (упорядоченные, НЕИЗМЕНЯЕМЫЕ) ---
coordinates = (10, 20, 30)
index_of_20 = coordinates.index(20)

# --- СЛОВАРИ / DICTIONARIES (пары Ключ: Значение) ---
capitals = {"USA": "Washington", "France": "Paris", "Japan": "Tokyo"}

capital_usa = capitals.get("USA")    # Безопасное получение значения
capitals.update({"Germany": "Berlin"}) # Добавление/обновление
capitals.pop("France")               # Удаление по ключу

# Итерация по словарю
for country, capital in capitals.items():
    print(f"{country}: {capital}")


# ==============================================================================
# 9. ГЕНЕРАТОРЫ СПИСКОВ (List Comprehensions)
# ==============================================================================

# Формула: [выражение for элемент in последовательность if условие]
doubled_numbers = [x * 2 for x in range(1, 6)]              # [2, 4, 6, 8, 10]
even_numbers = [x for x in range(1, 10) if x % 2 == 0]      # [2, 4, 6, 8]


# ==============================================================================
# 10. ФУНКЦИИ (Functions, *args, **kwargs)
# ==============================================================================

# Базовая функция с аннотацией типов и значениями по умолчанию
def multiply(a: float, b: float = 1.0) -> float:
    """Возвращает произведение чисел a и b."""
    return a * b

# *args — сжимает позиционные аргументы в кортеж (tuple)
def sum_all(*args: float) -> float:
    return sum(args)

# **kwargs — сжимает именованные аргументы в словарь (dict)
def print_user_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(sum_all(1, 2, 3, 4))
print_user_info(name="Alex", role="Developer")


# ==============================================================================
# 11. ОБРАБОТКА ИСКЛЮЧЕНИЙ (Exception Handling)
# ==============================================================================

try:
    number = int("123")
    result = 10 / 2
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: неверный формат числа!")
else:
    print("Ошибок не возникло, результат:", result)
finally:
    print("Блок finally выполняется всегда.")


# ==============================================================================
# 12. ОСНОВЫ ООП (Classes & OOP)
# ==============================================================================

class Car:
    # Переменная класса (общая для всех экземпляров)
    total_cars = 0

    def __init__(self, make: str, model: str, year: int):
        # Переменные экземпляра (уникальные для каждого объекта)
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1

    def drive(self) -> None:
        print(f"{self.make} {self.model} едет.")

# Наследование (Inheritance)
class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_size: int):
        super().__init__(make, model, year)
        self.battery_size = battery_size

# Создание объектов
car1 = Car("Toyota", "Camry", 2022)
tesla = ElectricCar("Tesla", "Model 3", 2024, 75)

car1.drive()
tesla.drive()