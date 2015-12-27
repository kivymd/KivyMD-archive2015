# -*- coding: utf-8 -*-
'''
Bottom Sheets
=============

`Material Design spec Bottom Sheets page <http://www.google.com/design/spec/components/bottom-sheets.html>`_

In this module there's the :class:`BottomSheet` class which will let you implement your own BottomSheets, and there are two classes called :class:`ListBottomSheet` and :class:`GridBottomSheet` implementing the ones mentioned in the spec.

Examples
--------

.. note::

    These widgets are designed to be called from Python code only.

For :class:`ListBottomSheet`:

.. code-block:: python

    bs = ListBottomSheet()
    bs.add_item("Here's an item with text only", lambda x: x)
    bs.add_item("Here's an item with an icon", lambda x: x, icon='md-cast')
    bs.add_item("Here's another!", lambda x: x, icon='md-nfc')
    bs.open()

For :class:`ListBottomSheet`:

.. code-block:: python

    bs = GridBottomSheet()
    bs.add_item("Facebook", lambda x: x, icon_src='./assets/facebook-box.png')
    bs.add_item("YouTube", lambda x: x, icon_src='./assets/youtube-play.png')
    bs.add_item("Twitter", lambda x: x, icon_src='./assets/twitter.png')
    bs.add_item("Da Cloud", lambda x: x, icon_src='./assets/cloud-upload.png')
    bs.add_item("Camera", lambda x: x, icon_src='./assets/camera.png')
    bs.open()
'''
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from kivymd.backgroundcolorbehavior import BackgroundColorBehavior
from kivymd.label import MaterialLabel
from kivymd.list import MaterialList, OneLineListItem, ILeftBody, \
	OneLineIconListItem
from kivymd.theming import ThemableBehavior

Builder.load_string('''
<BottomSheet>
	background: 'atlas://data/images/defaulttheme/action_group_disabled'
	background_color: 0,0,0,.8
	sv: sv
	upper_padding: upper_padding
	gl_content: gl_content
	ScrollView:
		id: sv
		do_scroll_x: False
		BoxLayout:
			size_hint_y: None
			orientation: 'vertical'
			padding: 0,1,0,0
			height: upper_padding.height + gl_content.height + 1  # +1 to allow overscroll
			BsPadding:
				id: upper_padding
				size_hint_y: None
				height: root.height - min(root.width * 9 / 16, gl_content.height)
				on_release: root.dismiss()
			BottomSheetContent:
				id: gl_content
				size_hint_y: None
				background_color: root.theme_cls.bg_normal
				cols: 1
''')


class BsPadding(ButtonBehavior, FloatLayout):
	pass


class BottomSheetContent(BackgroundColorBehavior, GridLayout):
	pass


class BottomSheet(ThemableBehavior, ModalView):
	sv = ObjectProperty()
	upper_padding = ObjectProperty()
	gl_content = ObjectProperty()
	dismiss_zone_scroll = 1000  # Arbitrary high number

	def open(self, *largs):
		super(BottomSheet, self).open(*largs)
		Clock.schedule_once(self.set_dismiss_zone, 0)

	def set_dismiss_zone(self, *largs):
		# Scroll to right below overscroll threshold:
		self.sv.scroll_y = 1 - self.sv.convert_distance_to_scroll(0, 1)[1]

		# This is a line where m (slope) is 1/6 and b (y-intercept) is 80:
		self.dismiss_zone_scroll = self.sv.convert_distance_to_scroll(
				0, (self.height - self.upper_padding.height) * (1 / 6.0) + 80)[
			1]
		# Uncomment next line if the limit should just be half of
		# visible content on open (capped by specs to 16 units to width/9:
		# self.dismiss_zone_scroll = (self.sv.convert_distance_to_scroll(
		# 		0, self.height - self.upper_padding.height)[1] * 0.50)

		# Check if user has overscrolled enough to dismiss bottom sheet:
		self.sv.bind(on_scroll_stop=self.check_if_scrolled_to_death)

	def check_if_scrolled_to_death(self, *largs):
		if self.sv.scroll_y >= 1 + self.dismiss_zone_scroll:
			self.dismiss()

	def add_widget(self, widget, index=0):
		if type(widget) == ScrollView:
			super(BottomSheet, self).add_widget(widget, index)
		else:
			self.gl_content.add_widget(widget, index)


Builder.load_string('''
#:import md_icons kivymd.icon_definitions.md_icons
<ListBSIconLeft>
	font_style: 'Icon'
	text: u"{}".format(md_icons[root.icon])
	halign: 'center'
	theme_text_color: 'Primary'
	valign: 'middle'
''')


class ListBSIconLeft(ILeftBody, MaterialLabel):
	icon = StringProperty()


class ListBottomSheet(BottomSheet):
	mlist = ObjectProperty()

	def __init__(self, **kwargs):
		super(ListBottomSheet, self).__init__(**kwargs)
		self.mlist = MaterialList()
		self.gl_content.add_widget(self.mlist)
		Clock.schedule_once(self.resize_content_layout, 0)

	def resize_content_layout(self, *largs):
		self.gl_content.height = self.mlist.height

	def add_item(self, text, callback, icon=None):
		if icon:
			item = OneLineIconListItem(text=text, on_release=callback)
			item.add_widget(ListBSIconLeft(icon=icon))
		else:
			item = OneLineListItem(text=text, on_release=callback)

		item.bind(on_release=lambda x: self.dismiss())
		self.mlist.add_widget(item)


Builder.load_string('''
<GridBSItem>
	orientation: 'vertical'
	padding: 0, dp(24), 0, 0
	size_hint_y: None
	size: dp(64), dp(96)
	BoxLayout:
		padding: dp(8), 0, dp(8), dp(8)
		size_hint_y: None
		height: dp(48)
		Image:
			source: root.source
	MaterialLabel:
		font_style: 'Caption'
		theme_text_color: 'Secondary'
		text: root.caption
		halign: 'center'
''')


class GridBSItem(ButtonBehavior, BoxLayout):
	source = StringProperty()

	caption = StringProperty()


class GridBottomSheet(BottomSheet):
	def __init__(self, **kwargs):
		super(GridBottomSheet, self).__init__(**kwargs)
		self.gl_content.padding = (dp(16), 0, dp(16), dp(24))
		self.gl_content.height = dp(24)
		self.gl_content.cols = 3

	def add_item(self, text, callback, icon_src):
		item = GridBSItem(
				caption=text,
				on_release=callback,
				source=icon_src
		)
		item.bind(on_release=lambda x: self.dismiss())
		if len(self.gl_content.children) % 3 == 0:
			self.gl_content.height += dp(96)
		self.gl_content.add_widget(item)
