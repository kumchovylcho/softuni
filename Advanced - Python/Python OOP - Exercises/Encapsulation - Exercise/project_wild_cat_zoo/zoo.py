class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = sum(x.salary for x in self.workers)
        if self.__budget >= all_salaries:
            self.__budget -= all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed_to_tend = sum(x.money_for_care for x in self.animals)
        if self.__budget >= money_needed_to_tend:
            self.__budget -= money_needed_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animals = {
            "Lion": [], "Tiger": [], "Cheetah": []
        }

        return self.get_status(self.animals, animals, "animals")

    def workers_status(self):
        workers = {
            "Keeper": [], "Caretaker": [], "Vet": []
        }

        return self.get_status(self.workers, workers, "workers")

    @staticmethod
    def get_status(collection: list, options: dict, status_for: str):
        for obj in collection:
            options[type(obj).__name__].append(obj.__repr__())
        output = [f"You have {len(collection)} {status_for}"]
        for key, value in options.items():
            output.append(f"----- {len(value)} {key + 's'}:")
            if value:
                for item in value:
                    output.append(item)
        return '\n'.join(output)

# class Zoo:
#
#     def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
#         self.name = name
#         self.__budget = int(budget)
#         self.__animal_capacity = int(animal_capacity)
#         self.__workers_capacity = int(workers_capacity)
#         self.animals = []
#         self.workers = []
#
#     def add_animal(self, animal, price):
#         if self.__budget >= price and len(self.animals) < self.__animal_capacity:
#             self.__budget -= price
#             self.animals.append(animal)
#             return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
#         if self.__budget < price and len(self.animals) < self.__animal_capacity:
#             return "Not enough budget"
#         return "Not enough space for animal"
#
#     def hire_worker(self, worker):
#         if len(self.workers) < self.__workers_capacity:
#             self.workers.append(worker)
#             return f"{worker.name} the {worker.__class__.__name__} hired successfully"
#         return "Not enough space for worker"
#
#     def fire_worker(self, worker_name):
#         for worker in self.workers:
#             if worker.name == worker_name:
#                 self.workers.remove(worker)
#                 return f"{worker_name} fired successfully"
#         return f"There is no {worker_name} in the zoo"
#
#     def pay_workers(self):
#         all_salaries = sum([x.salary for x in self.workers])
#         if self.__budget >= all_salaries:
#             self.__budget -= all_salaries
#             return f"You payed your workers. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to pay your workers. They are unhappy"
#
#     def tend_animals(self):
#         take_care_money = sum(x.money_for_care for x in self.animals)
#         if self.__budget >= take_care_money:
#             self.__budget -= take_care_money
#             return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to tend the animals. They are unhappy."
#
#     def profit(self, amount):
#         self.__budget += amount
#
#     def animals_status(self):
#         info = {"Cheetah": [], "Tiger": [], "Lion": []}
#         [info[x.__class__.__name__].append(str(x)) for x in self.animals]
#         output = [f"You have {len(info['Cheetah']) + len(info['Tiger']) + len(info['Lion'])} animals",
#                   f"----- {len(info['Lion'])} Lions:", *info['Lion'],
#                   f"----- {len(info['Tiger'])} Tigers:", *info['Tiger'],
#                   f"----- {len(info['Cheetah'])} Cheetahs:", *info['Cheetah']]
#         return "\n".join(output)
#
#     def workers_status(self):
#         info = {"Keeper": [], "Vet": [], "Caretaker": []}
#         [info[x.__class__.__name__].append(str(x)) for x in self.workers]
#         output = [f"You have {len(info['Keeper']) + len(info['Vet']) + len(info['Caretaker'])} workers",
#                   f"----- {len(info['Keeper'])} Keepers:", *info['Keeper'],
#                   f"----- {len(info['Caretaker'])} Caretakers:", *info['Caretaker'],
#                   f"----- {len(info['Vet'])} Vets:", *info['Vet']]
#         return "\n".join(output)
