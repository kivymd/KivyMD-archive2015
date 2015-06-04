#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='kivymd',
	  version='0.1.0',
	  description='Set of widgets for Kivy inspired by Google\'s Material '
				  'Design',
	  author='Andrés Rodríguez',
	  author_email='andres.rodriguez@lithersoft.com',
	  url='https://github.com/mixedCase/kivymd',
	  packages=['kivymd'],
	  package_data={'kivymd': ['images/*.png', 'images/*.jpg', 'images/*.atlas', 'fonts/*.ttf']},
	  exclude_package_data={'': ['*.pyc']},
	  )
