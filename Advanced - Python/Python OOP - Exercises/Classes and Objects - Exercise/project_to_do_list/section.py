from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for info in self.tasks:
            if new_task.name in info.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task_ in self.tasks:
            if task_name == task_.name:
                task_.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for pos, tasks in enumerate(self.tasks):
            if tasks.completed:
                count += 1
                del self.tasks[pos]
        return f"Cleared {count} tasks."

    def view_section(self):
        output = f"Section {self.name}:\n"
        for info in self.tasks:
            output += f"{info.details()}\n"
        return output
