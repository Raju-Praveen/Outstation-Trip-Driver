from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.core.window import Window

a = "Chennai"


class HomeScreen(MDScreen):
	balance = 0
	def __init__(self, **kwargs):
		super(HomeScreen, self).__init__(**kwargs)
		self.balance = 400
		
		if self.balance >= 500:
			self.ids.eligible_mark.source = "green_circle.png"
		elif self.balance < 500:
			self.ids.eligible_mark.source = "red_circle.png"
			anim = Animation(value=0, d=0.7) + Animation(value=1, d=0.7)
			anim.repeat = True
			anim.start(self.ids.eligible_mark)
		else:
			print("Eligible Mark error")
		
	def anim_tab_bar(self, start, end, *args):
		anim = Animation(x_start=start, x_end=end, d=0.2)
		anim.start(self.ids.active_tab)
		
	def change_screen(self, screen, *args):
		change_to = f"{screen}_screen"
		self.manager.current = change_to
		self.manager.transition.direction = "left"
	
		
class EveryTrip(MDCard):
	dialog, start_loc, accept = None, a, "Accept"
	
	def __init__(self, **kwargs):
		super(EveryTrip, self).__init__(**kwargs)
		
		
class AvailableTrips(ScrollView):
	balance = 0
	def __init__(self, **kwargs):
		super(AvailableTrips, self).__init__(**kwargs)
		self.balance = 400
		
		if self.balance >= 500:
			self.gridlayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
			self.gridlayout.bind(minimum_height=self.gridlayout.setter('height'))
			
			for i in range(10):
				EveryTrip.start_loc = "Vellore"
				self.gridlayout.add_widget(EveryTrip())
				
			self.size_hint = (1, None)
			self.bar_color = (1, 1, 1, 1)
			self.bar_inactive_color = (1, 1, 1, 1)
			self.size = (Window.width, Window.height*0.825)
			self.add_widget(self.gridlayout)
            
		elif self.balance < 500:
			self.add_widget(MDLabel(text="Please recharge the wallet.", halign="center"))
			
			
class TripWidget(MDCard):
    def __init__(self, **kwargs):
        super(TripWidget, self).__init__(**kwargs)
		
		
class NavigationDrawerContent(MDBoxLayout):
	pass
	
	
class UpcomingTrips(ScrollView):
	def __init__(self, **kwargs):
		super(UpcomingTrips, self).__init__(**kwargs)
		self.gridlayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		self.gridlayout.bind(minimum_height=self.gridlayout.setter('height'))
		
		for i in range(1):
			EveryTrip.accept = "Detail"
			self.gridlayout.add_widget(EveryTrip())
			
		self.size_hint = (1, None)
		self.bar_color = (1, 1, 1, 1)
		self.bar_inactive_color = (1, 1, 1, 1)
		self.size = (Window.width, Window.height*0.825)
		self.add_widget(self.gridlayout)