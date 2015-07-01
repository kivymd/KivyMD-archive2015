# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivymd.elevationbehaviour import ElevationBehaviour
from kivymd.icon_definitions import md_icons
from kivymd.label import MaterialLabel
from kivymd.list import MaterialList, ListItem, LeftListItemBody
from kivymd.slidingpanel import SlidingPanel
from kivymd.theming import ThemableBehavior


Builder.load_string('''
<NavigationDrawer>
	_list: _list
	canvas:
		Color:
			rgba: root.theme_cls.bg_light
		Rectangle:
			size: root.size
			pos: root.pos
	Image:
		id: _header_bg
		size_hint_y: None
		height: 0 if self.source == '' or self.source == None else 9 * self.width / 16
		x: root.x
		y: root.height - self.height
		mipmap: True
		allow_stretch: True
		keep_ratio: False
	ScrollView:
		size_hint_y: None
		height: root.height - _header_bg.height - dp(8)
		pos: root.pos
		MaterialList:
			id: _list
''')


class NavigationDrawer(SlidingPanel, ThemableBehavior, ElevationBehaviour):
	'''Implementation of the Navigation Drawer pattern.'''

	header_img = StringProperty()

	_list = ObjectProperty()
	_header_bg = ObjectProperty()

	def add_widget(self, widget, index=0):
		if issubclass(widget.__class__, NavigationDrawerCategory):
			self._list.add_widget(widget, index)
		else:
			super(NavigationDrawer, self).add_widget(widget, index)

	def on_header_img(self, instance, value):
		self._header_bg.source = value


class NavigationDrawerCategory(MaterialList):

	def __init__(self, **kwargs):
		super(NavigationDrawerCategory, self).__init__(**kwargs)
		self.padding = (0, self.padding[1], 0, 0)


class NavigationDrawerButton(ListItem):

	icon = StringProperty()

	def __init__(self, **kwargs):
		super(NavigationDrawerButton, self).__init__(**kwargs)
		self.lbl_icon = LeftIcon(font_style='Icon',
		                         theme_text_color='Custom',
		                         text_color=(0,0,0,0.54))
		Clock.schedule_once(self.initialization_instructions)

	def initialization_instructions(self, _):
		self.add_widget(self.lbl_icon)
		self.on_icon(None, self.icon)

	def on_icon(self, instance, value):
		if value == '':
			self.left_container_size = None
		else:
			self.left_container_size = 'small'
			self.lbl_icon.text = u"{}".format(md_icons[value])

	def on_parent(self, instance, value):
		if not issubclass(value.__class__, NavigationDrawerCategory):
			raise Exception("NavigationDrawerButton may only be placed inside"
			                " a NavigationDrawerCategory widget")

class LeftIcon(LeftListItemBody, MaterialLabel):
	pass