# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.theming import ThemeManager
from kivymd.label import MaterialLabel
from kivymd.dialog import Dialog

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
	MaterialRaisedButton:
		id: raised_button
		text: "Open Dialog"
		size_hint: None, None
		size: dp(110), dp(36)
		pos_hint: {'center_x': 0.75, 'center_y': 0.75}
'''


class KitchenSink(App):
	theme_cls = ThemeManager()

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		content = MaterialLabel(font_style='Body1',
								theme_text_color='Secondary',
								text="This is a Dialog with a title and some text. That's pretty awesome right!",
								valign='top')

		content.bind(size=content.setter('text_size'))

		self.dialog = Dialog(title="This is a test dialog",
							 content=content,
							 size_hint=(.8, None),
							 height=dp(200),
							 auto_dismiss=False)

		self.dialog.add_action_button("Dismiss", action=lambda *x: self.dialog.dismiss())
		main_widget.ids.raised_button.bind(on_release=lambda *x: self.dialog.open())
		return main_widget

	def on_pause(self):
		return True

	def on_stop(self):
		pass


if __name__ == '__main__':
	KitchenSink().run()