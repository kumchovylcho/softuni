expected_total_sum = int(input())

product_count = 0

products_paid_with_cash = 0
products_paid_with_credit_card = 0

payments_with_cash = 0
payments_with_card = 0

total_sum_reached = False
command = input()
while command != "End":

    product_count += 1
    product_price = int(command)
    if product_count % 2 == 0:
        if product_price < 10:
            print(f'Error in transaction!')
            command = input()
            continue

        products_paid_with_credit_card += product_price
        payments_with_card += 1

    else:
        if product_price > 100:
            print(f'Error in transaction!')
            command = input()
            continue

        products_paid_with_cash += product_price
        payments_with_cash += 1

    print(f'Product sold!')
    total_product_value = products_paid_with_credit_card + products_paid_with_cash
    if total_product_value >= expected_total_sum:
        total_sum_reached = True
        break

    command = input()


if total_sum_reached:
    average_payment_with_cash = products_paid_with_cash / payments_with_cash
    average_payment_with_card = products_paid_with_credit_card / payments_with_card
    print(f'Average CS: {average_payment_with_cash:.2f}')
    print(f'Average CC: {average_payment_with_card:.2f}')
else:
    print(f'Failed to collect required money for charity.')

################################################################################################

# money_that_needs_to_be_collected = int(input())
# money_in_cash = 0
# money_with_credit_card = 0
# alternation_counter = 0
# paid_in_cash = 0
# paid_with_credit_card = 0
# is_end = False
# while money_in_cash + money_with_credit_card < money_that_needs_to_be_collected:
#     price_of_product = input()
#     if price_of_product == "End":
#         is_end = True
#         break
#     price_of_product = int(price_of_product)
#     alternation_counter += 1
#     if alternation_counter % 2 != 0:
#         if price_of_product > 100:
#             print("Error in transaction!")
#         else:
#             money_in_cash += price_of_product
#             paid_in_cash += 1
#             print("Product sold!")
#     else:
#         if price_of_product < 10:
#             print("Error in transaction!")
#         else:
#             money_with_credit_card += price_of_product
#             paid_with_credit_card += 1
#             print("Product sold!")
# if is_end:
#     print("Failed to collect required money for charity.")
# else:
#     average_payment_with_cash = money_in_cash / paid_in_cash
#     average_payment_with_credit_card = money_with_credit_card / paid_with_credit_card
#     print(f"Average CS: {average_payment_with_cash:.2f}")
#     print(f"Average CC: {average_payment_with_credit_card:.2f}")
