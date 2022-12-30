class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(str(x) for x in self.data[::-1])}]"


# class Stack:
#     data = []
#
#     def push(self, element):
#         Stack.data.append(element)
#
#     def pop(self):
#         return Stack.data.pop()
#
#     def top(self):
#         return Stack.data[-1]
#
#     def is_empty(self):
#         if Stack.data:
#             return False
#         return True
#
#     def __str__(self):
#         return f"[{', '.join(Stack.data[::-1])}]"
