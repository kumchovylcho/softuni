from abc import ABC, abstractmethod


class Validation:

    @staticmethod
    def check_object_type(obj, obj_type):
        if not isinstance(obj, obj_type):
            raise AssertionError(f"`worker` must be of type {obj_type}")


class Work(ABC):

    @abstractmethod
    def work(self):
        pass


class Eat(ABC):

    @abstractmethod
    def eat(self):
        pass


class Worker(Work, Eat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")


class SuperWorker(Work, Eat):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")


class Robot(Work):

    def work(self):
        print("I'm a robot. I'm working....")


class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):
    def set_worker(self, worker):
        Validation.check_object_type(worker, Work)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        Validation.check_object_type(worker, Eat)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()

break_manager = BreakManager()

work_manager.set_worker(Worker())

break_manager.set_worker(Worker())

work_manager.manage()

break_manager.lunch_break()

work_manager.set_worker(SuperWorker())

break_manager.set_worker(SuperWorker())

work_manager.manage()

break_manager.lunch_break()

work_manager.set_worker(Robot())

work_manager.manage()

try:

    break_manager.set_worker(Robot())

    break_manager.lunch_break()

except:
    pass
