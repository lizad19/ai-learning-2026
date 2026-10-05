tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Добавлено: {task}")

def show_tasks():
    print("Твои задачи:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Проверка
add_task("Выучить функции")
add_task("Сделать коммит")
add_task("Продолжить обучение AI")
show_tasks()