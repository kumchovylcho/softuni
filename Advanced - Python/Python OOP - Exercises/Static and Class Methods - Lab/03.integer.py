class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                          'L': 50, 'C': 100,
                          'D': 500, 'M': 1000}
        result = 0
        for index, symbol in enumerate(value):
            if index + 1 == len(value) or roman_numerals[symbol] >= roman_numerals[value[index + 1]]:
                result += roman_numerals[symbol]
            else:
                result -= roman_numerals[symbol]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if str(value).isdigit():
            return cls(int(value))
        return "wrong type"


# class Integer:
#
#     def __init__(self, value: int):
#         self.value = int(value)
#
#     @staticmethod
#     def from_float(float_value):
#         if isinstance(float_value, float):
#             return Integer(int(float_value))
#         return "value is not a float"
#
#     @staticmethod
#     def from_roman(value):
#         roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
#         'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
#                  'CD': 400, 'CM': 900}
#         i = 0
#         num = 0
#         while i < len(value):
#             if i + 1 < len(value) and value[i:i + 2] in roman:
#                 num += roman[value[i:i + 2]]
#                 i += 2
#             else:
#                 num += roman[value[i]]
#                 i += 1
#         return Integer(num)
#
#     @staticmethod
#     def from_string(value):
#         if str(value).isdigit():
#             return Integer(int(value))
#         return "wrong type"
