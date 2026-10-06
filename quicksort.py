def quicksort(nums: list[int]) -> list[int]:
    # Базовый случай рекурсии
    if len (nums) <= 1:
        return nums
    # Выбираем опорный элемент (pivot)
    pivot = nums[len(nums) // 2]
    # Делим элементы на 3 группы
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    # рекурсивно сортируем влево и вправо, затем склеиваем
    return quicksort(left) + middle + quicksort(right)

numbers = [7, 3, 5, 1, 6, 9, 8, 2, 4]
sorted_numbers = quicksort(numbers)

print(f'Исходный: {numbers}')
print(f'Результат: {sorted_numbers}')