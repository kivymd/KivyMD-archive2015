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
<MaterialCheckBox>:
	canvas:
		Clear
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

''')


class MaterialCheckBox(ThemableBehavior, CircularRippleBehavior, ToggleButtonBehavior, Label):
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

	def on_group(self, *largs):
		if self.group:
			self._icon_normal = u"{}".format(md_icons['md-radio-button-off'])
			self._icon_active = u"{}".format(md_icons['md-radio-button-on'])
		else:
			self._icon_normal = u"{}".format(md_icons['md-check-box-outline-blank'])
			self._icon_active = u"{}".format(md_icons['md-check-box'])
		super(MaterialCheckBox, self).on_group(*largs)

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
