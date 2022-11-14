import re
count_of_barcodes = int(input())
for _ in range(count_of_barcodes):
    current_barcode = input()
    pattern = re.compile(r'(@#{1,})(?P<barcode>[A-Z][A-Za-z\d]{4,}[A-Z])(@#{1,})')
    digits = re.compile(r'(?P<digits>\d+)')
    barcode_validation = list(pattern.finditer(current_barcode))
    digits_finder = list(digits.finditer(current_barcode))
    if barcode_validation:
        if digits_finder:
            digit = [digit['digits'] for digit in digits_finder]
            if digit:
                print(f"Product group: {''.join(digit)}")
        elif not digits_finder:
            print("Product group: 00")
    elif not barcode_validation:
        print("Invalid barcode")

# import re
# pattern = re.compile(r'@(#+)(?P<word>([A-Z])[a-zA-Z\d]{4,}([A-Z]))@(#+)')
# number_of_barcodes = int(input())
# for barcode in range(number_of_barcodes):
#     current_barcode = input()
#     matches = list(pattern.finditer(current_barcode))
#     if matches:
#         for match in matches:
#             product_group = ''
#             for character in match['word']:
#                 if character.isdigit():
#                     product_group += character
#             if not product_group:
#                 product_group += "0" * 2
#             print(f"Product group: {product_group}")
#     elif not matches:
#         print("Invalid barcode")