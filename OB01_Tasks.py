class Task:
    def __init__(self, about, deadline, place):

        self.about = about
        self.deadline = deadline
        self.place = place
        self.completed= False

    def finish_task(self):
        self.completed=True

    def __repr__(self):
        status = "выполнено" if self.completed else "не выполнено"
        return f"{self.about} со сроком {self.deadline} {status}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, about, deadline, place):
        task = Task(about, deadline, place)
        self.tasks.append(task)
        print(f"Добавлена новая задача {about} cо сроком {deadline}")

    def finish_tasks(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].finish_task()
        else:
            print("Неверный индекс задачи")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __repr__(self):
        return f"TaskManager({self.tasks})"

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Реабилитация", "05.08.2024","ЕКПЦ")
    manager.add_task("Анализы", "03.08.2024", "ДД")
    manager.add_task("ЛОР", "16.08.2024", "ДКБ11")

    print(f"\nСПИСОК ЗАДАЧ\n {manager.tasks}")

    manager.finish_tasks(1)
    print(f"\nОбновленный список ВСЕХ задач:\n {manager.tasks}")

    print("\nОбновленный список ТЕКУЩИХ задач:")
    for task in manager.get_pending_tasks():
        print(task)
