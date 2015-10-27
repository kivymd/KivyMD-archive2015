# -*- coding: utf-8 -*-
from collections import deque
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.material_resources import DEVICE_TYPE

Builder.load_string('''
#:import Window kivy.core.window.Window
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import MaterialFlatButton kivymd.button.MaterialFlatButton
#:import MaterialLabel kivymd.label.MaterialLabel
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE
<_SnackbarWidget>
	canvas:
		Color:
			rgb: get_color_from_hex('323232')
		Rectangle:
			size: self.size
			pos: self.pos
	size_hint_y: None
	size_hint_x: 1 if DEVICE_TYPE == 'mobile' else None
	height: dp(48) if _label.height < dp(48) else dp(80)
	width: dp(288) if (_label.width + _spacer.width + _button.width + dp(24) + root.padding_right) < dp(288) else dp(568) if (_label.width + _spacer.width + _button.width + dp(24) + root.padding_right) > dp(568) else (_label.width + _spacer.width + _button.width + dp(24) + root.padding_right)
	top: 0
	x: 0 if DEVICE_TYPE == 'mobile' else Window.width/2 - self.width/2
	MaterialLabel:
		id: _label
		text: root.text
		size_hint_x: 0
		x: root.x + dp(24)
		y: root.y
		max_lines: 2
		width: Window.width - root.padding_right - _button.width - _spacer.width - dp(24) if DEVICE_TYPE == 'mobile' else self.texture_size[0] if (dp(568) - root.padding_right - _button.width - _spacer.width - self.texture_size[0] - dp(24)) >= 0 else (dp(568) - root.padding_right - _button.width - _spacer.width - dp(24))
	BoxLayout:
		id: _spacer
		size_hint_x: 0
		right: _button.x
		width: 0
	MaterialFlatButton:
		id: _button
		text: root.button_text
		size_hint_x: 0
		right: root.right - root.padding_right
		center_y: root.center_y
		on_release: root.button_callback
''')


class _SnackbarWidget(FloatLayout):
	text = StringProperty()
	button_text = StringProperty()
	button_callback = ObjectProperty()
	duration = NumericProperty()
	padding_right = NumericProperty(dp(24))

	def __init__(self, text, duration, button_text='', button_callback=None,
	             **kwargs):
		super(_SnackbarWidget, self).__init__(**kwargs)
		self.text = text
		self.button_text = button_text
		self.button_callback = button_callback
		self.duration = duration
		self.ids['_label'].text_size = (None, None)

	def begin(self):
		if self.button_text == '':
			self.ids['_button'].width = 0
		else:
			self.ids['_spacer'].width = dp(16) if \
				DEVICE_TYPE == "mobile" else dp(40)
			self.padding_right = dp(16)
		Window.add_widget(self)
		anim = Animation(top=self.height, duration=.3, t='out_quad')
		anim.start(self)
		Clock.schedule_once(lambda dt: self.die(), self.duration)

	def die(self):
		anim = Animation(top=0, duration=.3, t='out_quad')
		anim.bind(on_complete=lambda *args: _play_next(self))
		anim.bind(on_complete=lambda *args: Window.remove_widget(self))
		anim.start(self)


queue = deque()
playing = False


def make(text, button_text=None, button_callback=None, duration=3):
	if button_text is not None and button_callback is not None:
		queue.append(_SnackbarWidget(text=text,
		                             button_text=button_text,
		                             button_callback=button_callback,
		                             duration=duration))
	else:
		queue.append(_SnackbarWidget(text=text,
		                             duration=duration))
	_play_next()


def _play_next(dying_widget=None):
	global playing
	if (dying_widget or not playing) and len(queue) > 0:
		playing = True
		queue.popleft().begin()
	elif len(queue) == 0:
		playing = False
