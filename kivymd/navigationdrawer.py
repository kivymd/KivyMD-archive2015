# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.elevationbehaviour import ElevationBehaviour
from kivymd.icon_definitions import md_icons
from kivymd.label import MDLabel
from kivymd.list import OneLineIconListItem, ILeftBody, BaseListItem
from kivymd.slidingpanel import SlidingPanel
from kivymd.theming import ThemableBehavior

Builder.load_string('''
<NavigationDrawer>
	_list: _list
	canvas.before:
		Color:
			rgba: root.theme_cls.bg_light
		Rectangle:
			size: root.size
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
		id: _sv
		do_scroll_x: False
		height: root.height - _header_bg.height - dp(8)
		MDList:
			id: ml
			id: _list

<NavigationDrawerIconButton>
	NDIconLabel:
		id: _icon
		font_style: 'Icon'
		theme_text_color: 'Secondary'

''')


class NavigationDrawer(SlidingPanel, ThemableBehavior, ElevationBehaviour):
	'''Implementation of the Navigation Drawer pattern.'''

	header_img = StringProperty()

	_list = ObjectProperty()
	_header_bg = ObjectProperty()

	def __setattr__(self, key, value):
		if key == 'side':
			super(NavigationDrawer, self).__setattr__(key, 'left')
			return
		super(NavigationDrawer, self).__setattr__(key, value)

	def add_widget(self, widget, index=0):
		if issubclass(widget.__class__, BaseListItem):
			self._list.add_widget(widget, index)
			widget.bind(on_release=lambda x: self.toggle())
		else:
			super(NavigationDrawer, self).add_widget(widget, index)

	def on_header_img(self, instance, value):
		self._header_bg.source = value


class NDIconLabel(ILeftBody, MDLabel):
	pass


class NavigationDrawerIconButton(OneLineIconListItem):
	icon = StringProperty()

	def on_icon(self, instance, value):
		self.ids['_icon'].text = u"{}".format(md_icons[value])
