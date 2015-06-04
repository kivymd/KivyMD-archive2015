# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
#:import md_icons kivymd.icon_definitions.md_icons
#:import MaterialLabel kivymd.label.MaterialLabel
<MaterialIconButton>
	canvas:
		Color:
			rgba: 0,1,0,1
		Line:
			points: self.x,self.y, self.x+self.width,self.y, self.x+self.width,self.y+self.height, self.x,self.y+self.height, self.x,self.y
	size_hint: (None, None)
	size: (dp(48), dp(48))
	padding: dp(12)
	MaterialLabel:
		id: _label
		font_style: 'Icon'
		text: u"{}".format(md_icons[root.icon])
''')


class MaterialIconButton(ButtonBehavior, BoxLayout):
	icon = StringProperty('md-lens')
