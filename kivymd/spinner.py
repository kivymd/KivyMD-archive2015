# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.animation import Animation
from theming import ThemableBehavior

Builder.load_string('''
<MaterialSpinner>:
	canvas.before:
		PushMatrix
		Rotate:
			angle: self._rotation_angle
			origin: self.center
	canvas:
		Color:
			rgba: self.color
		Line:
			circle: self.center_x, self.center_y, self.width / 2, \
			self._angle_start, self._angle_end
			cap: 'round'
			width: dp(2)
	canvas.after:
		PopMatrix

''')


class MaterialSpinner(ThemableBehavior, Widget):
	color = ListProperty([])

	_rotation_angle = NumericProperty(360)
	_angle_start = NumericProperty(0)
	_angle_end = NumericProperty(45)

	def __init__(self, **kwargs):
		super(MaterialSpinner, self).__init__(**kwargs)
		self.color = self.theme_cls.primary_color
		_rot_anim = Animation(_rotation_angle=0,
		                      duration=3)
		_rot_anim.start(self)

		self._anim_start()

	def _anim_start(self, *args):
		_angle_start_anim = Animation(_angle_end=self._angle_end + 270,
		                              duration=.7,
		                              t='in_out_sine')
		_angle_start_anim.bind(on_complete=self._anim_back)
		_angle_start_anim.start(self)

	def _anim_back(self, *args):
		_angle_back_anim = Animation(_angle_start=self._angle_end - 8,
		                             duration=.7,
		                             t='in_out_sine')
		_angle_back_anim.bind(on_complete=self._anim_start)
		_angle_back_anim.start(self)

	def on__rotation_angle(self, *args):
		if self._rotation_angle == 0:
			self._rotation_angle = 360
			_rot_anim = Animation(_rotation_angle=0,
			                      duration=3)
			_rot_anim.start(self)
