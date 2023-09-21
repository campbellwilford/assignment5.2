import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

customer1 = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712',
                        'dsellyarft@gmpg.org', '254-555-9362', False)
customer2 = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710',
                        'ahimsworthfs@list-manage.com', '254-555-2273', True)

for trans_key, trans_data in dict.items():
    date, item_name, cost, customerid = trans_data
    if customerid == customer1.get_customerid():
        customer = customer1
    elif customerid == customer2.get_customerid():
        customer = customer2
    else:
        continue
    
    transaction = fc.Transaction(date, item_name, cost, customerid)
    order_total += cost
    
    print(f"Date: {transaction.get_date()}")
    print(f"Item: {transaction.item_name}")
    print(f"Cost: ${transaction.cost:.2f}")

if customer1.member_status or customer2.member_status:
    discount = order_total * 0.2
    order_total -= discount
    print(f"Discount Applied: ${discount:.2f}")

print(f"Order Total: ${order_total:.2f}")