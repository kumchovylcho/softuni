import re
pattern = re.compile(r'@(#+)(?P<word>([A-Z])[a-zA-Z\d]{4,}([A-Z]))@(#+)')
number_of_barcodes = int(input())
for barcode in range(number_of_barcodes):
    current_barcode = input()
    matches = list(pattern.finditer(current_barcode))
    if matches:
        for match in matches:
            product_group = ''
            for character in match['word']:
                if character.isdigit():
                    product_group += character
            if not product_group:
                product_group += "0" * 2
            print(f"Product group: {product_group}")
    elif not matches:
        print("Invalid barcode")