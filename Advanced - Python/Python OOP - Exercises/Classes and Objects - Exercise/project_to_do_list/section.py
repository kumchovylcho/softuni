from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for item in self.tasks:
            if item.name == task_name:
                item.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        for item in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[item].completed:
                cleared_tasks += 1
                self.tasks.pop(item)
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]
        for item in self.tasks:
            output.append(item.details())
        return '\n'.join(output)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())


# from project.task import Task
#
#
# class Section:
#
#     def __init__(self, name: str):
#         self.name = name
#         self.tasks = []
#
#     def add_task(self, new_task: Task):
#         for info in self.tasks:
#             if new_task.name in info.name:
#                 return f"Task is already in the section {self.name}"
#         self.tasks.append(new_task)
#         return f"Task {new_task.details()} is added to the section"
#
#     def complete_task(self, task_name: str):
#         for task_ in self.tasks:
#             if task_name == task_.name:
#                 task_.completed = True
#                 return f"Completed task {task_name}"
#         return f"Could not find task with the name {task_name}"
#
#     def clean_section(self):
#         count = 0
#         for pos, tasks in enumerate(self.tasks):
#             if tasks.completed:
#                 count += 1
#                 del self.tasks[pos]
#         return f"Cleared {count} tasks."
#
#     def view_section(self):
#         output = f"Section {self.name}:\n"
#         for info in self.tasks:
#             output += f"{info.details()}\n"
#         return output
