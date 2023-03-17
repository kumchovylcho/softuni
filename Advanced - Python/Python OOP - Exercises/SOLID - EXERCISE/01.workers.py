from abc import abstractmethod, ABC


class BaseWorker(ABC):

    @abstractmethod
    def work(self):
        pass


class Fisherman(BaseWorker):

    def work(self):
        print("A lot of work today! We caught a lot of fish!!!")


class Worker(BaseWorker):

    def work(self):
        print("I'm working!!")


class SuperWorker(BaseWorker):

    def work(self):
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, employee: BaseWorker):
        if not isinstance(employee, BaseWorker):
            raise AssertionError(f'`worker` must be of type {BaseWorker}')

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
