from tabulate import tabulate

class Membership:
    def __init__(self, username, monthly_income, monthly_expense, list_harga_barang):
        self.username = username
        self.monthly_income = monthly_income
        self.monthly_expense  = monthly_expense
        self.list_harga_barang = list_harga_barang

    #data existing user
    list_data_user = {
        'Sumbul': 'Platinum',
        'Ana': 'Gold',
        'Cahya': 'Platinum'
    }
    #list membership name
    list_membership = ['Platinum', 'Gold', 'Silver']

    #data benefit membership
    benefit = [
        ['Platinum', '15%','Benefit Silver + Gold + Voucher Liburan + Cashback Max. 30%'],
        ['Gold','10%','Benefit Silver + Voucher Ojek Online'],
        ['Silver','8%','Voucher Makanan']
    ]
    kolom_benefit = ['Membership','Discount','Another Benefit']
    benefit_membership = tabulate(benefit,kolom_benefit)

    #data requirement membership
    requirement = [
        ['Platinum',8,15],
        ['Gold',6,10],
        ['Silver',5,7]
    ]
    kolom_req = ['Membership','Monthly Expense (juta)', 'Monthly Income (juta)']
    req_membership = tabulate(requirement,kolom_req)

    def show_data(self):
        '''func show all data user'''
        print (self.list_data_user)
    def show_benefit(self):
        ''' func show all benefit membership'''
        print('Benefit Membership PacCommerce')
        print(self.benefit_membership)

    def show_requirements(self):
        ''' func show requirement all membership'''
        print('\nRequirements Membership PacCommerce')
        print(self.req_membership)

    def show_current_membership(self):
        ''' func show current membership'''
        name_membership = self.list_data_user.get(self.username)
        print(f'{self.username} saat ini {name_membership} membership')

    def predict_membership(self, monthly_income, monthly_expense):
        '''
        func to predict membership of customer
        input:
        (int) monthly_income
        (int) monthly_expense
        '''
        #menghitung distance seluruh membership
        distance = {}
        for row in self.requirement:
            dist = round(pow(((monthly_expense - row[1])**2) + ((monthly_income - row[2])**2),1/2),2)
            membership = row[0]
            distance.update({membership:dist})
        print(f'\nHasil perhitungan Euclidean Distance dari user {self.username} adalah {distance}')

        #mencari minimum distance untuk mendapat prediksi membership
        min_distance = min(distance, key=distance.get)
        print(f'{self.username} masuk ke membership {min_distance}\n')

        #update data user
        self.list_data_user.update({self.username:min_distance})



    def calculated_price(self,list_harga_barang):
        '''
        func menghitung total harga yang dibayarkan setelah diskon membership
        input:
        (list,int) list_harga_barang
        '''
        name_membership = self.list_data_user.get(self.username) #mencari nama membership
        idx_membership = self.list_membership.index(name_membership) #mencari benefit dr membership
        discount = int((self.benefit[idx_membership][1]).split('%')[0])/100 #mengambil discount dari benefit

        # total seluruh belanja
        total = 0
        for harga in list_harga_barang:
            total += harga

        #menghitng harga setelah discount
        final_price = total - (total*discount)
        print(f'\nHarga yang dibayarkan setelah discount {discount*100}% sebesar Rp {final_price}')
