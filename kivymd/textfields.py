# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty, NumericProperty, StringProperty, \
	ListProperty, BooleanProperty
from kivy.metrics import sp, dp
from kivy.animation import Animation
from kivymd.label import MaterialLabel
from theming import ThemableBehavior

Builder.load_string('''
<SingleLineTextField>:
    canvas.before:
    	Clear
        Color:
            rgba: self.line_color_normal
        Line:
            points: self.x, self.y + dp(8), self.x + self.width, self.y + dp(8)
            width: 1
            dash_length: dp(3)
            dash_offset: 2 if self.disabled else 0
		Color:
			rgba: self.error_color if self.error else self.line_color_focus
		Rectangle:
			size: self._line_width, dp(2)
			pos: self.center_x - (self._line_width / 2), self.y + dp(8)
        Color:
            rgba: self.error_color if self.error else (1, 1, 1, 0)
        Rectangle:
            texture: self._msg_label.texture
            size: self._msg_label.texture_size
            pos: self.x, self.y - dp(8)
        Color:
            rgba: (self.cursor_color if self.focus and not self.cursor_blink \
            else (0, 0, 0, 0))
        Rectangle:
            pos: [int(x) for x in self.cursor_pos]
            size: 1, -self.line_height
		Color:
			rgba: self._hint_txt_color if not self.text and not self.focus \
			else (self.line_color_focus if not self.text or self.focus \
			else (1, 1, 1, 0))
		Rectangle:
			texture: self._hint_lbl.texture
			size: self._hint_lbl.texture_size
			pos: self.x, self.y + self._hint_y
		Color:
            rgba: self.disabled_foreground_color if self.disabled else \
            (self.hint_text_color if not self.text and not self.focus else \
            self.foreground_color)

	font_name:	'Roboto'
	font_size:	sp(16)
	bold:		False
	padding:	0, dp(16), 0, dp(10)
	multiline:	False
''')


class SingleLineTextField(ThemableBehavior, TextInput):
	error_message = StringProperty('')

	line_color_normal = ListProperty([])
	line_color_focus = ListProperty([])

	error_color = ListProperty([])

	error = BooleanProperty(False)

	_hint_txt_color = ListProperty()
	_hint_lbl = ObjectProperty()
	_hint_lbl_font_size = NumericProperty(sp(16))
	_hint_y = NumericProperty(dp(10))
	_msg_label = ObjectProperty()
	_line_width = NumericProperty(0)
	_hint_txt = StringProperty('')

	def __init__(self, **kwargs):
		self._msg_label = MaterialLabel(font_style='Caption',
		                                theme_text_color='Error',
		                                halign='left',
		                                valign='middle')

		self._hint_lbl = MaterialLabel(font_style='Subhead',
		                               halign='left',
		                               valign='middle')
		super(SingleLineTextField, self).__init__(**kwargs)
		self.line_color_normal = self.theme_cls.divider_color
		self.line_color_focus = self.theme_cls.primary_color
		self.error_color = self.theme_cls.error_color
		self._hint_txt_color = self.theme_cls.disabled_hint_text_color
		self.hint_text_color = (1, 1, 1, 0)
		self.cursor_color = self.theme_cls.primary_color

		self.bind(error_message=self._set_msg,
		          hint_text=self._set_hint,
		          _hint_lbl_font_size=self._hint_lbl.setter('font_size'))

	def on_hint_text_color(self, instance, color):
		self._hint_txt_color = self.theme_cls.disabled_hint_text_color
		self.hint_text_color = (1, 1, 1, 0)

	def on_width(self, instance, width):
		self.anim = Animation(_line_width=width, duration=.2, t='out_quad')
		self._msg_label.width = self.width
		self._hint_lbl.width = self.width

	def on_pos(self, *args):
		self.hint_anim_in = Animation(_hint_y=dp(34),
		                              _hint_lbl_font_size=sp(12), duration=.2,
		                              t='out_quad')
		self.hint_anim_out = Animation(_hint_y=dp(10),
		                               _hint_lbl_font_size=sp(16),
		                               duration=.2,
		                               t='out_quad')

	def on_focus(self, *args):
		if self.focus:
			Animation.cancel_all(self, '_line_width', '_hint_y',
			                     '_hint_lbl_font_size')
			if len(self.text) == 0:
				self.hint_anim_in.start(self)
			if not self.error:
				self.anim.start(self)
		else:
			Animation.cancel_all(self, '_line_width', '_hint_y',
			                     '_hint_lbl_font_size')
			if len(self.text) == 0:
				self.hint_anim_out.start(self)
			if not self.error:
				self._line_width = 0

	def _set_hint(self, instance, text):
		self._hint_lbl.text = text

	def _set_msg(self, instance, text):
		self._msg_label.text = text
