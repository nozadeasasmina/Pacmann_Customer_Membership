from customer_membership import Membership

#user1 = Membership('Beta',12,9)
#user1.show_benefit()
#user1.show_requirements()
#user1.predict_membership(12,9)
#user1.show_data()
#user1.calculated_price([10000,10000])
#user1.show_current_membership()

user2 = Membership('Bambang', 4,3,[300_000, 150_000, 1_250_000, 15_000])
user2.show_benefit()
user2.show_requirements()
user2.predict_membership(4,3)
user2.show_data()
user2.calculated_price([300_000, 150_000, 1_250_000, 15_000])
user2.show_current_membership()