# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BoundedNumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.backgroundcolorbehavior import BackgroundColorBehavior
from kivymd.ripplebehavior import CircularRippleBehavior, \
	RectangularRippleBehavior
from kivymd.theming import ThemableBehavior

Builder.load_string('''
#:import md_icons kivymd.icon_definitions.md_icons
#:import MaterialLabel kivymd.label.MaterialLabel
<MaterialIconButton>
	size_hint: (None, None)
	size: (dp(48), dp(48))
	padding: dp(12)
	MaterialLabel:
		id: _label
		font_style: 'Icon'
		text: u"{}".format(md_icons[root.icon])

<MaterialFlatButton>
	size_hint: (None, None)
	height: dp(36)
	width: _label.texture_size[0] + dp(16)
	padding: (dp(8), 0)
	MaterialLabel:
		id: _label
		font_style: 'Button'
		size_hint_x: None
		text_size: (None, root.height)
		height: self.texture_size[1]
		theme_text_color: 'Primary'
		valign: 'middle'
		halign: 'center'
		opposite_colors: root.opposite_colors
''')


class MaterialIconButton(CircularRippleBehavior, ButtonBehavior, BoxLayout):
	icon = StringProperty('md-lens')


class MaterialFlatButton(ThemableBehavior, RectangularRippleBehavior,
                         ButtonBehavior, BackgroundColorBehavior, AnchorLayout):
	width = BoundedNumericProperty(dp(64), min=dp(64), max=None,
	                               errorhandler=lambda x: dp(64))

	text = StringProperty('')

	def __init__(self, **kwargs):
		super(MaterialFlatButton, self).__init__(**kwargs)
		Clock.schedule_once(lambda x: self.ids._label.bind(
			texture_size=self.update_width_on_label_texture))

	def update_width_on_label_texture(self, instance, value):
		self.ids['_label'].width = value[0]

	def on_text(self, instance, value):
		self.ids['_label'].text = value.upper()


class MaterialRaisedButton(MaterialFlatButton):
	# FIXME: Add elevation behavior
	pass