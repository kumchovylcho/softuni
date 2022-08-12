number = int(input())


def convert(n):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teen_numbers = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    round_numbers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    text = ""
    if n < 10:
        text = digits[n % 10]
    elif n <= 19:
        text = teen_numbers[n % 10]
    elif n <= 99 and n % 10 == 0:
        text = round_numbers[(n // 10) - 2]
    elif n <= 99 and n % 10 != 0:
        text = round_numbers[(n // 10) - 2] + " " + digits[n % 10]
    else:
        text = "one hundred"
    return text


print(convert(number))