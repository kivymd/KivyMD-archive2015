# -*- coding: utf-8 -*-
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import OptionProperty, NumericProperty, StringProperty, \
	BooleanProperty
from kivy.uix.relativelayout import RelativeLayout


class SlidingPanel(RelativeLayout):

	side = OptionProperty('left', options=['left', 'right'])
	animation_length_open = NumericProperty(0.3)
	animation_length_close = NumericProperty(0.3)
	animation_t_open = StringProperty('out_sine')
	animation_t_close = StringProperty('out_sine')
	nav_width = NumericProperty(dp(320))
	bind_to_window = BooleanProperty(True)

	_open = False
	_initial_x = 0

	def __init__(self, **kwargs):
		super(SlidingPanel, self).__init__(**kwargs)
		self.size_hint_x = None
		self.width = self.nav_width
		Clock.schedule_once(self.bind_to_window_if_requested)

	def bind_to_window_if_requested(self, _):
		if self.bind_to_window:
			Window.add_widget(self)

	def on_parent(self, instance, value):
		if issubclass(value.__class__, RelativeLayout) or value == Window:
			self.y = 0
			if self.side == 'left':
				self.x = -self.nav_width
			else:
				self.x = value.width
		else:
			self.y = value.y
			if self.side == 'left':
				self.x = value.x - self.nav_width
			else:
				self.x = value.x + value.width
		self._initial_x = self.x

	def toggle(self):
		Animation.stop_all(self, 'x')
		anim = self.animation_for_toggling_state()
		self._open = not self._open
		anim.start(self)

	def animation_for_toggling_state(self):
		if self._open:
			duration = self.animation_length_close
			t = self.animation_t_close
			x = self._initial_x
		else:
			duration = self.animation_length_open
			t = self.animation_t_open
			if self.side == 'left':
				x = self._initial_x + self.nav_width
			else:
				x = self._initial_x - self.nav_width
		anim = Animation(duration=duration, t=t, x=x)
		return anim

	def on_touch_down(self, touch):
		# Prevents touch events from propagating to anything below the widget.
		super(SlidingPanel, self).on_touch_down(touch)
		if self.collide_point(*touch.pos):
			return True