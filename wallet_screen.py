from kivymd.uix.screen import MDScreen


class WalletScreen(MDScreen):
	def __init__(self, **kwargs):
		super(WalletScreen, self).__init__(**kwargs)
		self.ids.balance_text.balance = "654"