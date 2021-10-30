from kivymd.uix.screen import MDScreen


class AboutUsScreen(MDScreen):
	call_no, whatsapp_no = "9941421552", "7010900496"
	
	def __init__(self, **kwargs):
		super(AboutUsScreen, self).__init__(**kwargs)