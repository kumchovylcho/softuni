class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        output = 1
        for number in args:
            output *= number
        return output

    @staticmethod
    def divide(*args):
        result = args[0]
        for number in args[1:]:
            if number > 0:
                result /= number
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for number in args[1:]:
            result -= number
        return result
