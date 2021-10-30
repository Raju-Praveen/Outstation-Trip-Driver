from kivymd.uix.screen import MDScreen


class ProfileScreen(MDScreen):
	wallet_balance, profile_picture = 500, "amazon_pay.png"
	user_name, mobile_no, vehicle_no, license_no, aadhar_no = "Praveen", "9876543210", "TN54X2166", "ABCD123456EF", "4531 5099 1502"
	
	def __init__(self, **kwargs):
		super(ProfileScreen, self).__init__(**kwargs)