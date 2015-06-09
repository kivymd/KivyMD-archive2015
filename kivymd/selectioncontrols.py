# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.properties import AliasProperty, BooleanProperty
from kivy.metrics import dp, sp
from kivymd.ripplebehavior import CircularRippleBehavior
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivymd.icon_definitions import md_icons
from theming import ThemableBehavior

Builder.load_string('''
<MaterialCheckbox>:
	canvas:
		Clear
		Color:
			rgba: self.background_color_disabled if self.disabled else \
			(self.background_color if self.active else self.background_color_down)
		Rectangle:
			size: 		self.size
			pos: 		self.pos
		Color:
			rgba: 		self.color
		Rectangle:
			texture:	self.texture
			size:		self.texture_size
			pos:		int(self.center_x - self.texture_size[0] / 2.), int(self.center_y - self.texture_size[1] / 2.)

	text: 			self._icon_active if self.active else self._icon_normal
	font_name:		'Icons'
	font_size:		sp(24)
	color:			self.theme_cls.primary_color if self.active else self.theme_cls.secondary_text_color
	halign:			'center'
	valign:			'middle'

'''

class MaterialCheckBox(ThemableBehavior, CircularRippleBehavior, ToggleButtonBehavior, Label):

	_bg_color_down = ListProperty([1, 1, 1, 0])
	def _get_bg_color_down(self):
		return self._bg_color_down

	def _set_bg_color_down(self, color, alpha=None):
		if len(color) == 2:
			self._bg_color_down = get_color_from_hex(colors[color[0]][color[1]])
			if alpha:
				self._bg_color_down[3] = alpha
		elif len(color) == 4:
			self._bg_color_down = color

	background_color_down = AliasProperty(_get_bg_color_down, _set_bg_color_down,
										  bind=('_bg_color_down', ))

	_bg_color_disabled = ListProperty([1, 1, 1, 0])
	def _get_bg_color_disabled(self):
		return self._bg_color_disabled

	def _set_bg_color_disabled(self, color, alpha=None):
		if len(color) == 2:
			self._bg_color_disabled = get_color_from_hex(colors[color[0]][color[1]])
			if alpha:
				self._bg_color_down[3] = alpha
		elif len(color) == 4:
			self._bg_color_disabled = color
	background_color_disabled = AliasProperty(_get_bg_color_disabled, _set_bg_color_disabled,
											  bind=('_bg_color_disabled', ))

	active = BooleanProperty(False)

	_icon_normal = StringProperty(u"{}".format(md_icons['md-check-box-outline-blank']))
	_icon_active = StringProperty(u"{}".format(md_icons['md-check-box']))

	def __init__(self, **kwargs):
		super(MaterialCheckBox, self).__init__(**kwargs)
		self.register_event_type('on_active')
		self.check_anim_out = Animation(font_size=0, duration=.1, t='out_quad')
		self.check_anim_in = Animation(font_size=sp(24), duration=.1, t='out_quad')
		self.check_anim_in.bind(on_complete=self._set_state)
		self.check_anim_out.bind(on_complete=lambda *x: self.check_anim_in.start(self))

	def on_release(self):
		Animation.cancel_all(self, '_size')
		self.check_anim_out.start(self)

	def _set_state(self, *args):
		if self.state == 'down':
			self.active = True
		else:
			self.active = False

	def on_active(self, instance, value):
		self.state = 'down' if value else 'normal'