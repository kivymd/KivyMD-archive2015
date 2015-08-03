# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import (ListProperty, ObjectProperty, NumericProperty,
                             OptionProperty)
from kivy.properties import AliasProperty
from kivy.metrics import dp

Builder.load_string('''
<ElevationBehaviour>:
	canvas:
		StencilPush
		Rectangle:
			size: self._stencil_size
			pos: self._stencil_pos
		StencilUse
		Color:
			a: self._soft_shadow_a
		Rectangle:
			texture: self._soft_shadow_texture
			size: self._soft_shadow_size
			pos: self._soft_shadow_pos
		Color:
			a: self._hard_shadow_a
		Rectangle:
			texture: self._hard_shadow_texture
			size: self._hard_shadow_size
			pos: self._hard_shadow_pos
		StencilUnUse
		StencilPop
		Color:
			a: 1


<RoundElevationBehaviour>:
	canvas:
		Color:
			a: self._soft_shadow_a
		Rectangle:
			texture: self._soft_shadow_texture
			size: self._soft_shadow_size
			pos: self._soft_shadow_pos
		Color:
			a: self._hard_shadow_a
		Rectangle:
			texture: self._hard_shadow_texture
			size: self._hard_shadow_size
			pos: self._hard_shadow_pos
		Color:
			a: 1
''')


class ElevationBehaviour(object):
	""":class:`ElevationBehaviour` is an attempt to implement the 3D look in
	Google's Material Design. This is not a correct shadow projection, it
	doesn't care about the elevation of underlying widgets and there it doesn't
	detect the shape of the widget.

	The shadow effect is made by several images with a black rectangle that's
	more or less blurred. In Material Design, there's two light sources that
	casts shadows. Here we have two images, one for the 'soft shadow' with more
	blur and one for the 'hard shadow' with less blur.

	Since most widgets used in Material Design are either rectangular or
	circular, we have made two implementations for one of each shape.

	With :attr:`cut_shadow` we can simulate the case of a widget being at the
	same level as another widget by cropping the shadow at either side. The
	:class:`NavigationDrawer` for instance, that is on the same 'height' as
	the :class:`ToolBar`, has this attribute set to 'top' so that no shadow
	is visible above it.

	..note::
		:attr:`cut_shadow` only works on widgets with static elevations. If
		the attr:`elevation` is animated, there's no shadow appearing on the
		side where it is cropped. That's something we will try to figure out
		how to implement.
	"""

	_elevation = NumericProperty(1)

	def _get_elevation(self):
		return self._elevation

	def _set_elevation(self, elevation):
		try:
			self._elevation = elevation
		except:
			self._elevation = 1

	elevation = AliasProperty(_get_elevation, _set_elevation,
	                          bind=('_elevation',))
	"""By increasing the :attr:`elevation` of a widget the shadow become larger
	 and 'softer', making it appear more or less elevated from its background.

	This can be animated to have the widget 'moving' on the z-axis.

	:attr:`elevation` is a :class:`~kivy.properties.AliasPropery` and
	defaults to 1
	"""

	cut_shadow = OptionProperty('no_cut', options=('no_cut', 'top',
	                                               'right', 'bottom',
	                                               'left'))
	"""The attr:`cut_shadow` can be set to 'no_cut', 'top', 'right', 'bottom',
	or 'left' in order to remove the shadow from either side. This can be used
	when you want the widget to appear on the same 'height' as a widget next to
	it.

	:attr:`determinate` is a :class:`~kivy.properties.OptionProperty` and
	defaults to 'no_cut'.
	"""

	_soft_shadow_texture = ObjectProperty()
	_soft_shadow_size = ListProperty([0, 0])
	_soft_shadow_pos = ListProperty([0, 0])
	_soft_shadow_a = NumericProperty(0)
	_hard_shadow_texture = ObjectProperty()
	_hard_shadow_size = ListProperty([0, 0])
	_hard_shadow_pos = ListProperty([0, 0])
	_hard_shadow_a = NumericProperty(0)
	_stencil_size = ListProperty([0, 0])
	_stencil_pos = ListProperty([0, 0])

	def __init__(self, **kwargs):
		super(ElevationBehaviour, self).__init__(**kwargs)
		self.bind(elevation=self._update_shadow,
		          pos=self._update_shadow,
		          size=self._update_shadow,
		          cut_shadow=self._update_shadow)

	def _update_shadow(self, *args):
		if self.elevation > 0:
			ratio = self.width / self.height
			if ratio > -2 and ratio < 2:
				self._shadow = App.get_running_app().theme_cls.quad_shadow
				width = soft_width = self.width * 1.9
				height = soft_height = self.height * 1.9
			elif ratio <= -2:
				self._shadow = App.get_running_app().theme_cls.rec_st_shadow
				ratio = abs(ratio)
				if ratio > 5:
					ratio = ratio * 22
				else:
					ratio = ratio * 11.5

				width = soft_width = self.width * 1.9
				height = self.height + dp(ratio)
				soft_height = self.height + dp(ratio) + dp(self.elevation) * .5
			else:
				self._shadow = App.get_running_app().theme_cls.rec_shadow
				ratio = abs(ratio)
				if ratio > 5:
					ratio = ratio * 22
				else:
					ratio = ratio * 11.5

				width = self.width + dp(ratio)
				soft_width = self.width + dp(ratio) + dp(self.elevation) * .9
				height = soft_height = self.height * 1.9

			x = self.center_x - width / 2
			soft_x = self.center_x - soft_width / 2
			self._soft_shadow_size = (soft_width, soft_height)
			self._hard_shadow_size = (width, height)

			y = self.center_y - soft_height / 2 - dp(
				.1 * 1.5 ** self.elevation)
			self._soft_shadow_pos = (soft_x, y)
			self._soft_shadow_a = 0.1 * 1.1 ** self.elevation
			self._soft_shadow_texture = self._shadow.textures[
				str(int(round(self.elevation - 1)))]

			y = self.center_y - height / 2 - dp(.5 * 1.18 ** self.elevation)
			self._hard_shadow_pos = (x, y)
			self._hard_shadow_a = .4 * .9 ** self.elevation
			self._hard_shadow_texture = self._shadow.textures[
				str(int(round(self.elevation)))]

			if self.cut_shadow == 'no_cut':
				self._stencil_size = self._soft_shadow_size
				self._stencil_pos = self._soft_shadow_pos
			elif self.cut_shadow == 'top':
				self._stencil_size = (self._soft_shadow_size[0] + self.width,
				                      self._soft_shadow_size[1] + self.height)
				self._stencil_pos = (self._soft_shadow_pos[0],
				                     self.y - self._soft_shadow_size[1])
			elif self.cut_shadow == 'right':
				self._stencil_size = (self._soft_shadow_size[0] + self.width,
				                      self._soft_shadow_size[1] + self.height)
				self._stencil_pos = (self.x - self._soft_shadow_size[0],
				                     self._soft_shadow_pos[1])
			elif self.cut_shadow == 'bottom':
				self._stencil_size = (self._soft_shadow_size[0] + self.width,
				                      self._soft_shadow_size[1] + self.height)
				self._stencil_pos = (self._soft_shadow_pos[0],
				                     self.y)
			elif self.cut_shadow == 'left':
				self._stencil_size = (self._soft_shadow_size[0] + self.width,
				                      self._soft_shadow_size[1] + self.height)
				self._stencil_pos = (self.x,
				                     self._soft_shadow_pos[1])

		else:
			self._soft_shadow_a = 0
			self._hard_shadow_a = 0


class RoundElevationBehaviour(object):
	_elevation = NumericProperty(1)

	def _get_elevation(self):
		return self._elevation

	def _set_elevation(self, elevation):
		try:
			self._elevation = elevation
		except:
			self._elevation = 1

	elevation = AliasProperty(_get_elevation, _set_elevation,
	                          bind=('_elevation',))

	_soft_shadow_texture = ObjectProperty()
	_soft_shadow_size = ListProperty([0, 0])
	_soft_shadow_pos = ListProperty([0, 0])
	_soft_shadow_a = NumericProperty(0)
	_hard_shadow_texture = ObjectProperty()
	_hard_shadow_size = ListProperty([0, 0])
	_hard_shadow_pos = ListProperty([0, 0])
	_hard_shadow_a = NumericProperty(0)

	def __init__(self, **kwargs):
		super(RoundElevationBehaviour, self).__init__(**kwargs)
		self._shadow = App.get_running_app().theme_cls.round_shadow
		self.bind(elevation=self._update_shadow,
		          pos=self._update_shadow,
		          size=self._update_shadow)

	def _update_shadow(self, *args):
		if self.elevation > 0:
			width = self.width * 2
			height = self.height * 2

			x = self.center_x - width / 2
			self._soft_shadow_size = (width, height)

			self._hard_shadow_size = (width, height)

			y = self.center_y - height / 2 - dp(.1 * 1.5 ** self.elevation)
			self._soft_shadow_pos = (x, y)
			self._soft_shadow_a = 0.1 * 1.1 ** self.elevation
			self._soft_shadow_texture = self._shadow.textures[
				str(int(round(self.elevation)))]

			y = self.center_y - height / 2 - dp(.5 * 1.18 ** self.elevation)
			self._hard_shadow_pos = (x, y)
			self._hard_shadow_a = .4 * .9 ** self.elevation
			self._hard_shadow_texture = self._shadow.textures[
				str(int(round(self.elevation - 1)))]

		else:
			self._soft_shadow_a = 0
			self._hard_shadow_a = 0
