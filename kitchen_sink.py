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
#:import MaterialCheckBox kivymd.selectioncontrols.MaterialCheckBox
#:import MaterialSwitch kivymd.selectioncontrols.MaterialSwitch
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
		elevation_normal: 2
		opposite_colors: True
		size_hint: None, None
		size: dp(110), dp(36)
		pos_hint: {'center_x': 0.75, 'center_y': 0.75}
	MaterialCheckBox:
		id:			chkbox
		size_hint:	None, None
		size:		dp(48), dp(48)
		pos_hint:	{'center_x': 0.2, 'center_y': 0.65}
	MaterialCheckBox:
		id:			grp_chkbox_1
		group:		'test'
		size_hint:	None, None
		size:		dp(48), dp(48)
		pos_hint:	{'center_x': 0.4, 'center_y': 0.65}
	MaterialCheckBox:
		id:			grp_chkbox_2
		group:		'test'
		size_hint:	None, None
		size:		dp(48), dp(48)
		pos_hint:	{'center_x': 0.5, 'center_y': 0.65}
	MaterialSwitch:
		size_hint:	None, None
		size:		dp(36), dp(48)
		pos_hint:	{'center_x': 0.7, 'center_y': 0.65}
		active:		False
	FloatingActionButton:
		id:					float_act_btn
		icon:				'md-android'
		size_hint:			None, None
		size:				dp(56), dp(56)
		opposite_colors:	True
		elevation_normal:	8
		pos_hint:			{'center_x': 0.85, 'center_y': 0.1}

'''


class KitchenSink(App):
	theme_cls = ThemeManager()

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		# self.theme_cls.theme_style = 'Dark'
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
