def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Ошибка: делить на ноль нельзя"
    return a / b

# Проверяем работу функций
print("Сложение:", add(10, 5))
print("Умножение:", multiply(4, 7))
print("Вычитание:", subtract(20, 8))
print("Деление:", divide(15, 3))
print("Деление на ноль:", divide(10, 0))