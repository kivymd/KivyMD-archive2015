# -*- coding: utf-8 -*-
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, OptionProperty, \
	BooleanProperty
from kivy.uix.floatlayout import FloatLayout


class SlidingPanel(FloatLayout):

	side = OptionProperty('left', options=['left', 'right'])
	animation_length_open = NumericProperty(0.3)
	animation_length_close = NumericProperty(0.3)
	animation_t_open = StringProperty('out_sine')
	animation_t_close = StringProperty('out_sine')
	nav_width = NumericProperty(dp(320))
	bind_to_window = BooleanProperty(True)

	_open = False
	_animating = False
	_initial_x = 0

	def __init__(self, **kwargs):
		super(SlidingPanel, self).__init__(**kwargs)
		if self.bind_to_window:
			Window.add_widget(self)

	def attempt_to_set_initial_x(self):
		if not self._animating:
			if self._open:
				self._initial_x = self.x - self.nav_width
			else:
				self._initial_x = self.x

	def on_bind_to_window(self, instance, value):
		raise Exception("Property 'bind_to_window' can't be modified after "
		                "instantiation")

	def on_side(self, instance, value):
		raise Exception("Property 'side' can't be modified after "
		                "instantiation")

	def toggle(self):
		self.attempt_to_set_initial_x()
		Animation.stop_all(self, 'x')
		anim = self.animation_for_toggling_state()
		self._animating = True
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
		return Animation(duration=duration, t=t, x=x)

	def animation_cleanup(self):
		self._animating = False

	def on_touch_down(self, touch):
		# Prevents touch events from propagating to anything below the widget.
		super(SlidingPanel, self).on_touch_down(touch)
		if self.collide_point(*touch.pos):
			return True


class NavigationDrawer(SlidingPanel):
	pass