from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivy.animation import Animation

class SignInLoginScreen(MDScreen):
	
	def __init__(self, **kwargs):
		super(SignInLoginScreen, self).__init__(**kwargs)
		
	def signin_submit_action(self, mobile, email, password, *args):
		if len(mobile) == 10:
			if "@" in email:
				if len(password) >= 8:
					toast("Information Correct")
					Animation(x_pos=1.5, d=0.25).start(self.ids.signin_widget_container)
					Animation(x_pos=0.5, d=0.25).start(self.ids.otp_verification_widget_container)
					Animation(y_pos=-80, d=0.25).start(self.ids.already_user_widget_container)
					Animation(y_pos=1, d=0.25).start(self.ids.resend_otp_widget_container)
				else:
					toast("Password must be more than 8 letters.")
			else:
				toast("Please enter the correct email")
		else:
			toast("Please enter the correct mobile no.")
			
	def login_submit_action(self, email, password):
		if "@" in email:
			if len(password) >= 8:
				toast("Information Correct")
				Animation(x_pos=1.5, d=0.25).start(self.ids.login_widget_container)
				Animation(x_pos=0.5, d=0.25).start(self.ids.otp_verification_widget_container)
				Animation(y_pos=-80, d=0.25).start(self.ids.new_user_widget_container)
				Animation(y_pos=1, d=0.25).start(self.ids.resend_otp_widget_container)
			else:
				toast("Password must be more than 8 letters.")
		else:
			toast("Please enter the correct email")