# -*- coding: utf-8 -*-
import kivymd.snackbar as Snackbar
from kivy.app import App
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
#:import MaterialList kivymd.list.MaterialList
#:import NavigationDrawer kivymd.navigationdrawer.NavigationDrawer
#:import ListItem kivymd.list.ListItem
#:import SingleLineTextField kivymd.textfields.SingleLineTextField
#:import MDSpinner kivymd.spinner.MDSpinner

RelativeLayout:
	Toolbar:
		id: toolbar
		title: 'KivyMD Kitchen Sink'
		left_action_items: [['md-menu', lambda x: nav_drawer.toggle()]]
		right_action_items: [['md-content-copy', lambda x: None], \
		['md-more-vert', lambda x: None]]

	SingleLineTextField:
		id: text_field
		size_hint: 0.8, None
		height: dp(48)
		pos_hint: {'center_x': 0.5, 'center_y': 0.85}
		hint_text: "Write something"

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


	ScrollView:
		do_scroll_x: False
		pos_hint: {'center_x': 0.5, 'center_y': 0.4}
		size_hint: (None, None)
		size: (320, 250)
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

	MDSpinner:
		id: spinner
		size_hint: None, None
		size: dp(46), dp(46)
		pos_hint: {'center_x': 0.15, 'center_y': 0.1}
		determinate: True if chkbox.active else False

	MaterialLabel:
		font_style: 'Subhead'
		theme_text_color: 'Primary'
		text: "Determinate"
		halign: 'center'
		pos_hint: {'center_x': 0.5, 'center_y': 0.14}
	MaterialCheckBox:
		id:			chkbox
		size_hint:	None, None
		size:		dp(48), dp(48)
		pos_hint:	{'center_x': 0.5, 'center_y': 0.1}

	FloatingActionButton:
		id:					float_act_btn
		icon:				'md-replay'
		size_hint:			None, None
		size:				dp(56), dp(56)
		opposite_colors:	True
		elevation_normal:	8
		pos_hint:			{'center_x': 0.85, 'center_y': 0.1}
		on_release:         spinner.active = not spinner.active



	NavigationDrawer:
		id: nav_drawer
		bind_to_window: False
		size_hint_y: None
		height: root.height - toolbar.height
		NavigationDrawerCategory:
			NavigationDrawerButton:
				icon: 'md-lens'
				text: 'Item 1'
			NavigationDrawerButton:
				icon: 'md-lens'
				text: 'Item 2'
			NavigationDrawerButton:
				icon: 'md-lens'
				text: 'Item 3'
			NavigationDrawerButton:
				icon: 'md-lens'
				text: 'Item 4'
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
		main_widget.ids.flat_button.bind(on_release=lambda *x: Snackbar.make("This is a much longer snackbar with extra text! Extra text! Extra text! Extra text! Extra text!", button_text="Hello cruel world", button_callback=lambda *args: 2))
		main_widget.ids.text_field.bind(on_text_validate=self.set_error_message,
										on_focus=self.set_error_message)
		return main_widget

	def set_error_message(self, *args):
		if len(self.root.ids.text_field.text) == 0:
			self.root.ids.text_field.error = True
			self.root.ids.text_field.error_message = "Some text is required"
		else:
			self.root.ids.text_field.error = False

	def on_pause(self):
		return True

	def on_stop(self):
		pass


if __name__ == '__main__':
	KitchenSink().run()
