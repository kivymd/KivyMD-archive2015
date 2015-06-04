# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import OptionProperty, AliasProperty, ObjectProperty, \
	StringProperty
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivymd.material_resources import FONTS, DEVICE_TYPE

for font in FONTS:
	LabelBase.register(**font)


class ThemeManager(Widget):

	primary_palette = OptionProperty(
		'Blue',
		options=['Pink', 'Blue', 'Indigo', 'BlueGrey', 'Brown', 'LightBlue',
		         'Purple', 'Grey', 'Yellow', 'LightGreen', 'DeepOrange',
		         'Green', 'Red', 'Teal', 'Orange', 'Cyan', 'Amber',
		         'DeepPurple', 'Lime'])

	primary_hue = OptionProperty(
		'500',
		options=['50', '100', '200', '300', '400', '500', '600', '700', '800',
		         '900', 'A100', 'A200', 'A400', 'A700'])

	primary_light_hue = OptionProperty(
		'100',
		options=['50', '100', '200', '300', '400', '500', '600', '700', '800',
		         '900', 'A100', 'A200', 'A400', 'A700'])

	primary_dark_hue = OptionProperty(
		'700',
		options=['50', '100', '200', '300', '400', '500', '600', '700', '800',
		         '900', 'A100', 'A200', 'A400', 'A700'])

	def _get_primary_color(self):
		return get_color_from_hex(
			colors[self.primary_palette][self.primary_hue])

	primary_color = AliasProperty(_get_primary_color,
	                              bind=('primary_palette', 'primary_hue'))

	def _get_primary_light(self):
		return get_color_from_hex(
			colors[self.primary_palette][self.primary_light_hue])

	primary_light = AliasProperty(
		_get_primary_light, bind=('primary_palette', 'primary_light_hue'))

	def _get_primary_dark(self):
		return get_color_from_hex(
			colors[self.primary_palette][self.primary_dark_hue])

	primary_dark = AliasProperty(_get_primary_color,
	                              bind=('primary_palette', 'primary_dark_hue'))

	accent_palette = OptionProperty(
		'Amber',
		options=['Pink', 'Blue', 'Indigo', 'BlueGrey', 'Brown', 'LightBlue',
		         'Purple', 'Grey', 'Yellow', 'LightGreen', 'DeepOrange',
		         'Green', 'Red', 'Teal', 'Orange', 'Cyan', 'Amber',
		         'DeepPurple', 'Lime'])

	accent_hue = OptionProperty(
		'A200',
		options=['50', '100', '200', '300', '400', '500', '600', '700', '800',
		         '900', 'A100', 'A200', 'A400', 'A700'])

	accent_light_hue = OptionProperty(
		'A100',
		options=['50', '100', '200', '300', '400', '500', '600', '700', '800',
		         '900', 'A100', 'A200', 'A400', 'A700'])

	accent_dark_hue = OptionProperty(
		'A400',
		options=['50', '100', '200', '300', '400', '500', '600', '700', '800',
		         '900', 'A100', 'A200', 'A400', 'A700'])

	def _get_accent_color(self):
		return get_color_from_hex(
			colors[self.accent_palette][self.accent_hue])

	accent_color = AliasProperty(_get_accent_color,
	                             bind=['accent_palette', 'accent_hue'])

	def _get_accent_light(self):
		return get_color_from_hex(
			colors[self.accent_palette][self.accent_light_hue])

	accent_light = AliasProperty(_get_accent_light,
	                             bind=['accent_palette', 'accent_light_hue'])

	def _get_accent_dark(self):
		return get_color_from_hex(
			colors[self.accent_palette][self.accent_dark_hue])

	accent_dark = AliasProperty(_get_accent_dark,
	                            bind=['accent_palette', 'accent_dark_hue'])

	theme_style = OptionProperty('Light', options=['Light', 'Dark'])

	def _get_bg_darkest(self):
		if self.theme_style == 'Light':
			return get_color_from_hex(colors['Light']['StatusBar'])
		elif self.theme_style == 'Dark':
			return get_color_from_hex(colors['Dark']['StatusBar'])

	bg_darkest = AliasProperty(_get_bg_darkest, bind=['theme_style'])

	def _get_bg_dark(self):
		if self.theme_style == 'Light':
			return get_color_from_hex(colors['Light']['AppBar'])
		elif self.theme_style == 'Dark':
			return get_color_from_hex(colors['Dark']['AppBar'])

	bg_dark = AliasProperty(_get_bg_dark, bind=['theme_style'])

	def _get_bg_normal(self):
		if self.theme_style == 'Light':
			return get_color_from_hex(colors['Light']['Background'])
		elif self.theme_style == 'Dark':
			return get_color_from_hex(colors['Dark']['Background'])

	bg_normal = AliasProperty(_get_bg_normal, bind=['theme_style'])

	def _get_bg_light(self):
		if self.theme_style == 'Light':
			return get_color_from_hex(colors['Light']['CardsDialogs'])
		elif self.theme_style == 'Dark':
			return get_color_from_hex(colors['Dark']['CardsDialogs'])

	bg_light = AliasProperty(_get_bg_light, bind=['theme_style'])

	def _get_divider_color(self):
		if self.theme_style == 'Light':
			color = get_color_from_hex('000000')
		elif self.theme_style == 'Dark':
			color = get_color_from_hex('FFFFFF')
		color[3] = .12
		return color

	divider_color = AliasProperty(_get_divider_color, bind=['theme_style'])

	def _get_text_color(self):
		if self.theme_style == 'Light':
			color = get_color_from_hex('000000')
			color[3] = .87
		elif self.theme_style == 'Dark':
			color = get_color_from_hex('FFFFFF')
		return color

	text_color = AliasProperty(_get_text_color, bind=['theme_style'])

	def _get_secondary_text_color(self):
		if self.theme_style == 'Light':
			color = get_color_from_hex('000000')
			color[3] = .54
		elif self.theme_style == 'Dark':
			color = get_color_from_hex('FFFFFF')
			color[3] = .70
		return color

	secondary_text_color = AliasProperty(_get_secondary_text_color,
	                                     bind=['theme_style'])

	def _get_icon_color(self):
		if self.theme_style == 'Light':
			color = get_color_from_hex('000000')
			color[3] = .54
		elif self.theme_style == 'Dark':
			color = get_color_from_hex('FFFFFF')
		return color

	icon_color = AliasProperty(_get_icon_color,
	                           bind=['theme_style'])

	def _get_disabled_hint_text_color(self):
		if self.theme_style == 'Light':
			color = get_color_from_hex('000000')
			color[3] = .26
		elif self.theme_style == 'Dark':
			color = get_color_from_hex('FFFFFF')
			color[3] = .30
		return color

	disabled_hint_text_color = AliasProperty(_get_disabled_hint_text_color,
	                                         bind=['theme_style'])

	# Hardcoded because muh standard
	def _get_error_color(self):
		return get_color_from_hex(colors['Red', 'A700'])

	error_color = AliasProperty(_get_error_color)

	def _determine_device_orientation(self, _, window_size):
		if window_size[0] > window_size[1]:
			self.device_orientation = 'landscape'
		elif window_size[1] >= window_size [0]:
			self.device_orientation = 'portrait'

	device_orientation = StringProperty('')

	def _get_standard_increment(self):
		if DEVICE_TYPE == 'mobile':
			if self.device_orientation == 'landscape':
				return dp(48)
			else:
				return dp(56)
		else:
			return dp(64)

	standard_increment = AliasProperty(_get_standard_increment,
	                                   bind=['device_orientation'])

	def _get_horizontal_margins(self):
		if DEVICE_TYPE == 'mobile':
			return dp(16)
		else:
			return dp(24)
	horizontal_margins = AliasProperty(_get_horizontal_margins)

	def on_theme_style(self, instance, value):
		if hasattr(App.get_running_app(), 'theme_cls'):
			self.set_clearcolor_by_theme_style(value)

	def set_clearcolor_by_theme_style(self, theme_style):
		if theme_style == 'Light':
			Window.clearcolor = get_color_from_hex(
				colors['Light']['Background'])
		elif theme_style == 'Dark':
			Window.clearcolor = get_color_from_hex(
				colors['Dark']['Background'])

	def __init__(self, **kwargs):
		super(ThemeManager, self).__init__(**kwargs)
		if App.get_running_app() is None:
			self.set_clearcolor_by_theme_style(self.theme_style)
		self._determine_device_orientation(None, Window.size)
		Window.bind(size=self._determine_device_orientation)


class ThemableBehavior(object):
	theme_cls = ObjectProperty()

	def __init__(self, **kwargs):
		if hasattr(App.get_running_app(), 'theme_cls'):
			self.theme_cls = App.get_running_app().theme_cls
		else:
			self.theme_cls =ThemeManager()
		super(ThemableBehavior, self).__init__(**kwargs)
