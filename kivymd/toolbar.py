# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivymd.backgroundcolorbehavior import BackgroundColorBehavior
from kivymd.button import MaterialIconButton
from kivymd.theming import ThemableBehavior
from kivymd.elevationbehaviour import ElevationBehaviour

Builder.load_string('''
#:import m_res kivymd.material_resources
<Toolbar>
	size_hint_y: None
	pos_hint: {'center_y': 0.5}
	height: root.theme_cls.standard_increment
	background_color: root.theme_cls.primary_color
	elevation: 6
	BoxLayout:
		id: left_actions
		orientation: 'horizontal'
		size_hint: (None, None)
		height: dp(48)
		x: root.x + root.theme_cls.horizontal_margins - dp(12)
		y: root.y + root.height - (root.theme_cls.standard_increment - self.height)/2 - self.height
	BoxLayout:
		id: right_actions
		orientation: 'horizontal'
		size_hint: (None, None)
		height: dp(48)
		x: root.width - root.theme_cls.horizontal_margins + dp(12) - self.width
		y: root.y + root.height - (root.theme_cls.standard_increment - self.height)/2 - self.height
	MaterialLabel:
		size_hint_x: None
		width: right_actions.x - self.x - dp(12)
		x: root.x + left_actions.width + dp(24)
		y: root.y
		font_style: 'Title'
		opposite_colors: True
		text: root.title
''')


class Toolbar(ThemableBehavior, ElevationBehaviour, BackgroundColorBehavior, RelativeLayout):

	left_action_items = ListProperty()
	"""The icons on the left of the toolbar.

	To add one, append a list like the following:

		['icon_name', callback]

	where 'icon_name' is a string that corresponds to an icon definition and
	 callback is the function called on a touch release event.
	"""

	right_action_items = ListProperty()
	"""The icons on the left of the toolbar.

	Works the same way as :attr:`left_action_items`
	"""

	title = StringProperty()

	def __init__(self, **kwargs):
		super(Toolbar, self).__init__(**kwargs)
		Clock.schedule_once(
			lambda x: self.on_left_action_items(0, self.left_action_items))
		Clock.schedule_once(
			lambda x: self.on_right_action_items(0, self.right_action_items))

	def on_left_action_items(self, instance, value):
		self.update_action_bar(self.ids['left_actions'], value)

	def on_right_action_items(self, instance, value):
		self.update_action_bar(self.ids['right_actions'], value)

	def update_action_bar(self, action_bar, action_bar_items):
		action_bar.clear_widgets()
		new_width = 0
		for item in action_bar_items:
			new_width += dp(48)
			action_bar.add_widget(MaterialIconButton(icon=item[0],
			                                         on_release=item[1],
			                                         opposite_colors=True))
		action_bar.width = new_width
