from tabulate import tabulate

class Membership:
    def __init__(self, username, membership, monthly_income, monthly_expense, list_harga_barang):
        self.username = username
        self.membership = membership
        self.monthly_income = monthly_income
        self.monthly_expense  = monthly_expense
        self.list_harga_barang = list_harga_barang

    #data benefit membership
    benefit = [
        ['Platinum', '15%','Benefit Silver + Gold + Voucher Liburan + Cashback Max. 30%'],
        ['Silver','10%','Benefit Gold + Voucher Ojek Online'],
        ['Gold','8%','Voucher Makanan']
    ]
    kolom_benefit = ['Membership','Discount','Another Benefit']
    benefit_membership = tabulate(benefit,kolom_benefit)

    #data requirement membership
    requirement = [
        ['Platinum',8,15],
        ['Silver',6,10],
        ['Gold',5,7]
    ]
    kolom_req = ['Membership','Monthly Expense (juta)', 'Monthly Income (juta)']
    req_membership = tabulate(requirement,kolom_req)

    def show_benefit(self):
        ''' func show all benefit membership'''
        print(self.benefit_membership)

    def show_requirements(self):
        ''' func show requirement all emmbership'''
        print(self.req_membership)

    def predict_membership(self, monthly_income, monthly_expense):
        distance = []
        for row in [self.req_membership.index()]:
            #dist = (monthly_expense - self.req_membership[row][1])**2
            print(row )


