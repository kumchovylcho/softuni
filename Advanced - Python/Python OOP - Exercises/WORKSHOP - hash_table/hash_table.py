class HashTable:

    def __init__(self):
        self.table = [[] for _ in range(self.default_length)]
        self.item_counter = 0

    @property
    def default_length(self):
        return 4

    @property
    def multiply_table_length(self):
        return 2

    def double_table_space(self):
        new_length = len(self.table) * self.multiply_table_length
        new_table = [[] for _ in range(new_length)]

        for item in self.table:
            for key_value in item:
                index = hash(key_value[0]) % len(new_table)

                new_table[index].append(key_value)

        self.table = new_table


    def hash(self, key: str):
        return hash(key) % len(self.table)

    def add(self, key: str, value: any):
        index = self.hash(key)

        for key_value in self.table[index]:
            if key_value[0] == key:
                key_value[1] = value
                return

        self.table[index].append([key, value])
        self.item_counter += 1

        if self.item_counter > len(self.table):
            self.double_table_space()

    def get(self, key: str):
        index = self.hash(key)

        for key_value in self.table[index]:
            if key_value[0] == key:
                return key_value[1]

        raise KeyError('key does not exist')

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key: str):
        return self.get(key)
