# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, OptionProperty, \
	NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
import kivymd.material_resources as m_res
from kivymd.ripplebehavior import RectangularRippleBehavior
from kivymd.theming import ThemableBehavior

Builder.load_string('''
<MaterialList>
	cols: 1
	size_hint_y: None
	height: self._min_list_height
	padding: (0, self._list_vertical_padding, 0, self._list_vertical_padding)

<ListItem>
	size_hint_y: None
	_left_container: _left_container
	_text_container: _text_container
	_right_container: _right_container
	canvas:
		Color:
			rgba: self.theme_cls.divider_color
		Line:
			points: root.x,root.y, root.x+self.width,root.y
	BoxLayout:
		id: _left_container
		size_hint: (None, None)
		x: root.x + dp(16)
		y: root.y + root.height - root._txt_top_pad - self.height - dp(5) if root.type == 'three-line' else root.y + root.height/2 - self.height/2
		size: (0,0) if root.left_container_size is None else ((dp(40), dp(40)) if root.left_container_size is 'big' else (dp(24), dp(24)))
		canvas:
			Color:
				rgba: 1,0,1,1
			Rectangle:
				size: self.size
				pos: self.pos
	BoxLayout:
		#canvas:
		#	Color:
		#		rgba: 0,1,1,.8
		#	Line:
		#		points: root._txt_left_pad,root._txt_bot_pad, self.width-root._txt_right_pad,root._txt_bot_pad, self.width-root._txt_right_pad,self.height-root._txt_top_pad, root._txt_left_pad,self.height-root._txt_top_pad, root._txt_left_pad,root._txt_bot_pad
		id: _text_container
		orientation: 'vertical'
		pos: root.pos
		padding: (root._txt_left_pad, root._txt_top_pad, root._txt_right_pad, root._txt_bot_pad)
		MaterialLabel:
			id: _lbl_primary
			text: root.text
			font_style: 'Subhead'
			theme_text_color: 'Primary'
			size_hint_y: None
			height: self.texture_size[1]
		MaterialLabel:
			id: _lbl_secondary
			text: '' if root.type == 'one-line' else root.secondary_text
			font_style: 'Body1'
			theme_text_color: 'Secondary'
			size_hint_y: None
			height: 0 if root.type == 'one-line' else self.texture_size[1]
	BoxLayout:
		id: _right_container
		size_hint: (None, None)
		x: root.x + root.width - m_res.HORIZ_MARGINS - self.width
		y: root.y + root.height - root._txt_top_pad - self.height - dp(5) if root.type == 'three-line' else root.y + root.height/2 - self.height/2
		size: (dp(24),dp(24))
		opacity: 0 if root.right_container_size is None else 1
		disabled: True if root.right_container_size is None else False
		canvas:
			Color:
				rgba: 0,1,1,1
			Rectangle:
				size: self.size
				pos: self.pos
		Button:
			size: _right_container.size
''')


class MaterialList(GridLayout):
	selected = ObjectProperty()
	_min_list_height = dp(16)
	_list_vertical_padding = dp(8)

	icon = StringProperty()

	def __init__(self, **kwargs):
		super(MaterialList, self).__init__(**kwargs)

	def add_widget(self, widget, index=0):
		widget.bind(height=lambda x, y: self.resize())
		widget.bind(on_release=lambda x: widget.select(selection_tracker=self))
		super(MaterialList, self).add_widget(widget, index)
		self.resize()

	def remove_widget(self, widget):
		super(MaterialList, self).remove_widget(widget)
		self.resize()

	def clear_widgets(self, children=None):
		super(MaterialList, self).clear_widgets(children)
		self.resize()

	def register_new_selection(self, widget):
		if self.selected:
			self.selected.is_selected = False
		self.selected = widget

	def resize(self):
		new_height = self._min_list_height
		for i in self.children:
			if type(i) == ListItem:
				new_height += i.height
		self.height = new_height


class ListItem(ThemableBehavior, RectangularRippleBehavior,
               ButtonBehavior, FloatLayout):
	type = OptionProperty('one-line',
	                      options=['one-line', 'two-line', 'three-line'])

	left_container_size = OptionProperty(
		None, options=['small', 'big'], allownone=True)
	'''Size of the left widget container.

	Valid values are None (no container), \'small\' (24dp, e.g. icons) and
	 \'big\' (40dp, e.g. avatars, checkboxes,...)
	'''

	right_container_size = OptionProperty(
		None, options=['small'], allownone=True)
	'''Size of the right widget container.

	Valid values are None (no container) and \'small\' (24dp, e.g. icons).
	'''

	text = StringProperty()

	secondary_text = StringProperty()

	_txt_left_pad = NumericProperty()
	_txt_top_pad = NumericProperty()
	_txt_bot_pad = NumericProperty()
	_txt_right_pad = NumericProperty(m_res.HORIZ_MARGINS)
	_left_container = ObjectProperty()
	_right_container = ObjectProperty()

	def __init__(self, **kwargs):
		super(ListItem, self).__init__(**kwargs)
		self.on_left_container_size(None, self.left_container_size)

	def on_touch_down(self, touch):
		if self.propagate_touch_to_container_children(touch, 'down'):
			return
		super(ListItem, self).on_touch_down(touch)

	def on_touch_move(self, touch, *args):
		if self.propagate_touch_to_container_children(touch, 'move', *args):
			return
		super(ListItem, self).on_touch_move(touch, *args)

	def on_touch_up(self, touch):
		if self.propagate_touch_to_container_children(touch, 'up'):
			return
		super(ListItem, self).on_touch_up(touch)

	def propagate_touch_to_container_children(self, touch, touch_event, *args):
		children = []
		triggered = False
		try:
			children.append(self.ids['_left_container'].children[0])
		except:
			pass
		try:
			children.append(self.ids['_right_container'].children[0])
		except:
			pass
		for i in children:
			if issubclass(i.__class__, ButtonBehavior) and \
					i.collide_point(touch.x, touch.y):
				triggered = True
				if touch_event == 'down':
					i.on_touch_down(touch)
				elif touch_event == 'move':
					i.on_touch_move(touch, *args)
				elif touch_event == 'up':
					i.on_touch_up(touch)
		if triggered:
			return True
		else:
			return False

	def on_type(self, instance, value):
		if value == 'one-line':
			self.set_sizes_for_one_line()
		elif value == 'two-line':
			self.set_sizes_for_two_line()
		elif value == 'three-line':
			self.set_sizes_for_three_line()

	def on_left_container_size(self, instance, value):
		if value:
			self._txt_left_pad = dp(72)
		else:
			self._txt_left_pad = dp(16)
		self.on_type(None, self.type)

	def on_right_container_size(self, instance, value):
		if value:
			self._txt_right_pad =  dp(16) + dp(24) + m_res.HORIZ_MARGINS
		else:
			self._txt_right_pad = m_res.HORIZ_MARGINS

	def set_sizes_for_one_line(self):
		if self.left_container_size == 'big':
			self.height = dp(56)
			self._txt_top_pad = dp(20)
			self._txt_bot_pad = dp(24) - dp(5)
		else:
			self.height = dp(48)
			self._txt_top_pad = dp(16)
			self._txt_bot_pad = dp(20) - dp(5)

	def set_sizes_for_two_line(self):
		self.height = dp(72)
		self._txt_top_pad = dp(20)
		self._txt_bot_pad = dp(20) - dp(5)

	def set_sizes_for_three_line(self):
		self.height = dp(88)
		self._txt_top_pad = dp(16)
		self._txt_bot_pad = dp(20) - dp(5)

	def select(self, selection_tracker):
		pass
