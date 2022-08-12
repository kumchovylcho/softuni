name_of_air_company = input()
tickets_for_adults = int(input())
tickets_for_children = int(input())
net_price_ticket_adult = float(input())
price_tax_service = float(input())
net_price_ticket_children = (net_price_ticket_adult - (net_price_ticket_adult * 0.7)) + price_tax_service
net_price_ticket_adult += price_tax_service
total_price_all_tickets = (tickets_for_adults * net_price_ticket_adult) + (tickets_for_children * net_price_ticket_children)
profit = total_price_all_tickets * 0.2
print(f"The profit of your agency from {name_of_air_company} tickets is {profit:.2f} lv.")