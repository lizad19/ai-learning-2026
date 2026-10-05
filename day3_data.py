# 1. Список студентов
students = ["Анна", "Игорь", "Мария", "Дмитрий", "Ольга"]

print("Список студентов:")
for student in students:
    print("-", student)

print()  # пустая строка

# 2. Словарь с оценками
grades = {
    "Анна": 9,
    "Игорь": 7,
    "Мария": 10,
    "Дмитрий": 6,
    "Ольга": 8
}

print("Оценки студентов:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

print()

# 3. Средний балл
total = 0
for grade in grades.values():
    total += grade

average = total / len(grades)
print("Средний балл:", round(average, 2))

# 4. Кто получил 8 и выше
print("\nСтуденты с оценкой 8 и выше:")
for name, grade in grades.items():
    if grade >= 8:
        print(f"{name} — {grade}")

# Самая высокая и самая низкая оценка
max_grade = max(grades.values())
min_grade = min(grades.values())

print("\nСамая высокая оценка:", max_grade)
print("Самая низкая оценка:", min_grade)

print("\nКто получил максимум:")
for name, grade in grades.items():
    if grade == max_grade:
        print(name)

print("\nКто получил минимум:")
for name, grade in grades.items():
    if grade == min_grade:
        print(name)        