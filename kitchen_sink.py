# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivymd.theming import ThemeManager

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MaterialList kivymd.list.MaterialList
#:import ListItem kivymd.list.ListItem
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
	ScrollView:
		do_scroll_x: False
		pos_hint: {'center_x': 0.3, 'center_y': 0.3}
		size_hint: (None, None)
		size: (320, 300)
		MaterialList:
			ListItem:
				type: 'one-line'
				text: 'Single-line item'
			ListItem:
				type: 'two-line'
				text: 'Two-line item'
				secondary_text: 'Secondary text here'
			ListItem:
				type: 'three-line'
				text: 'Three-line item'
				secondary_text: 'This is a multi-line label where you can fit more text than usual'
			ListItem:
				type: 'one-line'
				left_container_size: 'small'
				text: 'Single-line item'
			ListItem:
				type: 'two-line'
				left_container_size: 'small'
				text: 'Two-line item'
				secondary_text: 'Secondary text here'
			ListItem:
				type: 'three-line'
				left_container_size: 'small'
				text: 'Three-line item'
				secondary_text: 'This is a multi-line label where you can fit more text than usual'
			ListItem:
				type: 'one-line'
				left_container_size: 'big'
				text: 'Single-line item'
			ListItem:
				type: 'two-line'
				left_container_size: 'big'
				text: 'Two-line item'
				secondary_text: 'Secondary text here'
			ListItem:
				type: 'three-line'
				left_container_size: 'big'
				text: 'Three-line item'
				secondary_text: 'This is a multi-line label where you can fit more text than usual'
			ListItem:
				type: 'one-line'
				right_container_size: 'small'
				text: 'Single-line item'
			ListItem:
				type: 'two-line'
				right_container_size: 'small'
				text: 'Two-line item'
				secondary_text: 'Secondary text here'
			ListItem:
				type: 'three-line'
				right_container_size: 'small'
				text: 'Three-line item'
				secondary_text: 'This is a multi-line label where you can fit more text than usual'
			ListItem:
				type: 'one-line'
				left_container_size: 'small'
				right_container_size: 'small'
				text: 'Single-line item'
			ListItem:
				type: 'two-line'
				left_container_size: 'small'
				right_container_size: 'small'
				text: 'Two-line item'
				secondary_text: 'Secondary text here'
			ListItem:
				type: 'three-line'
				left_container_size: 'small'
				right_container_size: 'small'
				text: 'Three-line item'
				secondary_text: 'This is a multi-line label where you can fit more text than usual'
			ListItem:
				type: 'one-line'
				left_container_size: 'big'
				right_container_size: 'small'
				text: 'Single-line item'
			ListItem:
				type: 'two-line'
				left_container_size: 'big'
				right_container_size: 'small'
				text: 'Two-line item'
				secondary_text: 'Secondary text here'
			ListItem:
				type: 'three-line'
				left_container_size: 'big'
				right_container_size: 'small'
				text: 'Three-line item'
				secondary_text: 'This is a multi-line label where you can fit more text than usual'
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