class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status

    def get_customerid(self):
        return self.customerid

class Transaction:
    def __init__(self, date, item_name, cost, customerid):
        self.date = date
        self.item_name = item_name
        self.cost = cost
        self.customerid = customerid

    def get_date(self):
        return self.date
