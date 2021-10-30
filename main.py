from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from signin_login_screen import SignInLoginScreen
from home_screen import HomeScreen
from profile_screen import ProfileScreen
from wallet_screen import WalletScreen
from aboutus_screen import AboutUsScreen
from upcoming_trip_detail import UpComingTripDetail


class Main(MDApp):
	def build(self):
		sm = ScreenManager()
		#sm.add_widget(SignInLoginScreen(name="signin_login_screen"))
		sm.add_widget(HomeScreen(name="home_screen"))
		sm.add_widget(ProfileScreen(name="profile_screen"))
		sm.add_widget(WalletScreen(name="wallet_screen"))
		sm.add_widget(AboutUsScreen(name="aboutus_screen"))
		sm.add_widget(UpComingTripDetail(name="upcoming_trip_detail_screen"))
		
		
		return sm
		
		
if __name__ == "__main__":
	Main().run()