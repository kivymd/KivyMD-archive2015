# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.theming import ThemeManager

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
RelativeLayout:
	Toolbar:
		title: 'KivyMD Kitchen Sink'
		left_action_items: [['md-menu', lambda x: None]]
		right_action_items: [['md-content-copy', lambda x: None], \
		['md-more-vert', lambda x: None]]
	MaterialFlatButton:
		id: flat_button
		text: 'MaterialFlatButton'
		pos_hint: {'center_x': 0.3, 'center_y': 0.75}
'''


class KitchenSink(App):
	theme_cls = ThemeManager()

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		return main_widget

	def on_pause(self):
		return True

	def on_stop(self):
		pass


if __name__ == '__main__':
	KitchenSink().run()