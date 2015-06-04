# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.ripplebehavior import RectangularRippleBehavior

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
''')


class MaterialIconButton(RectangularRippleBehavior, ButtonBehavior, BoxLayout):
	icon = StringProperty('md-lens')