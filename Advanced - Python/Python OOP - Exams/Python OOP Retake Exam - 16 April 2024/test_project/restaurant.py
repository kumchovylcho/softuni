class Restaurant:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.waiters = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Invalid name!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Invalid capacity!")
        self.__capacity = value

    def get_waiters(self, min_earnings=None, max_earnings=None):
        filtered_waiters = [waiter for waiter in self.waiters
                            if (min_earnings is None or waiter.get('total_earnings', 0) >= min_earnings) and
                            (max_earnings is None or waiter.get('total_earnings', 0) <= max_earnings)]
        return filtered_waiters

    def add_waiter(self, waiter_name):
        if len(self.waiters) == self.capacity:
            return "No more places!"

        if waiter_name in (existing_waiter['name'] for existing_waiter in self.waiters):
            return f"The waiter {waiter_name} already exists!"

        new_waiter = {'name': waiter_name}
        self.waiters.append(new_waiter)
        return f"The waiter {waiter_name} has been added."

    def remove_waiter(self, waiter_name):
        for waiter in self.waiters:
            if waiter['name'] == waiter_name:
                self.waiters.remove(waiter)
                return f"The waiter {waiter_name} has been removed."
        return f"No waiter found with the name {waiter_name}."

    def get_total_earnings(self):
        return sum(waiter.get('total_earnings', 0) for waiter in self.waiters)


