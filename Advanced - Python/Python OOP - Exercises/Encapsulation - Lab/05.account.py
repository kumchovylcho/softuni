class Account:

    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if self.__pin == pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"
