# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.properties import BoundedNumericProperty, ReferenceListProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.elevationbehaviour import ElevationBehaviour
from kivymd.theming import ThemableBehavior

Builder.load_string('''
<MDCard>
	canvas:
		Color:
			rgba: self.background_color
		RoundedRectangle:
			size: self.size
			pos: self.pos
			radius: [dp(3)]
	background_color: self.theme_cls.bg_light
''')


class MDCard(ThemableBehavior, ElevationBehaviour, BoxLayout):
	r = BoundedNumericProperty(1., min=0., max=1.)
	g = BoundedNumericProperty(1., min=0., max=1.)
	b = BoundedNumericProperty(1., min=0., max=1.)
	a = BoundedNumericProperty(0., min=0., max=1.)

	background_color = ReferenceListProperty(r, g, b, a)
