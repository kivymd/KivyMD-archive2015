# -*- coding: utf-8 -*-
import kivymd.snackbar as Snackbar
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivymd.selectioncontrols import MDCheckbox
from kivymd.theming import ThemeManager
from kivymd.dialog import MDDialog

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import NavigationDrawer kivymd.navigationdrawer.NavigationDrawer
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import SingleLineTextField kivymd.textfields.SingleLineTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors

RelativeLayout:
	Toolbar:
		id: toolbar
		title: 'KivyMD Kitchen Sink'
		left_action_items: [['md-menu', lambda x: nav_drawer.toggle()]]
		right_action_items: [['md-more-vert', lambda x: None]]
	ScreenManager:
		id: scr_mngr
		size_hint_y: None
		height: root.height - toolbar.height
		Screen:
			name: 'bottomsheet'
			MDRaisedButton:
				text: "Open list bottom sheet"
				opposite_colors: True
				size_hint: None, None
				size: 4 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.6}
				on_release: app.show_example_bottom_sheet()
			MDRaisedButton:
				text: "Open list bottom sheet"
				opposite_colors: True
				size_hint: None, None
				size: 4 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.3}
				on_release: app.show_example_grid_bottom_sheet()
		Screen:
			name: 'button'
			MDFlatButton:
				text: 'MDFlatButton'
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.75}
			MDRaisedButton:
				text: "MDRaisedButton"
				elevation_normal: 2
				opposite_colors: True
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}
			MDFloatingActionButton:
				id:					float_act_btn
				icon:				'md-replay'
				size_hint:			None, None
				size:				dp(56), dp(56)
				opposite_colors:	True
				elevation_normal:	8
				pos_hint:			{'center_x': 0.5, 'center_y': 0.25}

		Screen:
			name: 'card'
			MDCard:
				size_hint: None, None
				size: dp(320), dp(180)
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}

		Screen:
			name: 'dialog'
			MDRaisedButton:
				text: "Open dialog"
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}
				opposite_colors: True
				on_release: app.show_example_dialog()
		Screen:
			name: 'list'
			ScrollView:
				do_scroll_x: False
				MDList:
					id: ml
					OneLineListItem:
						text: "One-line item"
					TwoLineListItem:
						text: "Two-line item"
						secondary_text: "Secondary text here"
					ThreeLineListItem:
						text: "Three-line item"
						secondary_text: "This is a multi-line label where you can fit more text than usual"
					OneLineAvatarListItem:
						text: "Single-line item with avatar"
						AvatarSampleWidget:
							source: './assets/avatar.png'
					TwoLineAvatarListItem:
						type: "two-line"
						text: "Two-line item..."
						secondary_text: "with avatar"
						AvatarSampleWidget:
							source: './assets/avatar.png'
					ThreeLineAvatarListItem:
						type: "three-line"
						text: "Three-line item..."
						secondary_text: "...with avatar..." + '\\n' + "and third line!"
						AvatarSampleWidget:
							source: './assets/avatar.png'
					OneLineIconListItem:
						text: "Single-line item with left icon"
						IconLeftSampleWidget:
							id: li_icon_1
							icon: 'md-stars'
					TwoLineIconListItem:
						text: "Two-line item..."
						secondary_text: "...with left icon"
						IconLeftSampleWidget:
							id: li_icon_2
							icon: 'md-chat'
					ThreeLineIconListItem:
						text: "Three-line item..."
						secondary_text: "...with left icon..." + '\\n' + "and third line!"
						IconLeftSampleWidget:
							id: li_icon_3
							icon: 'md-sd-storage'
					OneLineAvatarIconListItem:
						text: "Single-line + avatar&icon"
						AvatarSampleWidget:
							source: './assets/avatar.png'
						IconRightSampleWidget:
					TwoLineAvatarIconListItem:
						text: "Two-line item..."
						secondary_text: "...with avatar&icon"
						AvatarSampleWidget:
							source: './assets/avatar.png'
						IconRightSampleWidget:
					ThreeLineAvatarIconListItem:
						text: "Three-line item..."
						secondary_text: "...with avatar&icon..." + '\\n' + "and third line!"
						AvatarSampleWidget:
							source: './assets/avatar.png'
						IconRightSampleWidget:

		Screen:
			name: 'menu'
			MDRaisedButton:
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				text: 'Open menu'
				opposite_colors: True
				pos_hint: {'center_x': 0.1, 'center_y': 0.9}
				on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
			MDRaisedButton:
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				text: 'Open menu'
				opposite_colors: True
				pos_hint: {'center_x': 0.1, 'center_y': 0.1}
				on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
			MDRaisedButton:
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				text: 'Open menu'
				opposite_colors: True
				pos_hint: {'center_x': 0.9, 'center_y': 0.1}
				on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
			MDRaisedButton:
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				text: 'Open menu'
				opposite_colors: True
				pos_hint: {'center_x': 0.9, 'center_y': 0.9}
				on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
			MDRaisedButton:
				size_hint: None, None
				size: 3 * dp(48), dp(48)
				text: 'Open menu'
				opposite_colors: True
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}
				on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)

		Screen:
			name: 'progress'
			MDCheckbox:
				id:			chkbox
				size_hint:	None, None
				size:		dp(48), dp(48)
				pos_hint:	{'center_x': 0.5, 'center_y': 0.4}
				active: True
			MDSpinner:
				id: spinner
				size_hint: None, None
				size: dp(46), dp(46)
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}
				active: True if chkbox.active else False

		Screen:
			name: 'selectioncontrols'
			MDCheckbox:
				id:			grp_chkbox_1
				group:		'test'
				size_hint:	None, None
				size:		dp(48), dp(48)
				pos_hint:	{'center_x': 0.25, 'center_y': 0.5}
			MDCheckbox:
				id:			grp_chkbox_2
				group:		'test'
				size_hint:	None, None
				size:		dp(48), dp(48)
				pos_hint:	{'center_x': 0.5, 'center_y': 0.5}
			MDSwitch:
				size_hint:	None, None
				size:		dp(36), dp(48)
				pos_hint:	{'center_x': 0.75, 'center_y': 0.5}
				active:		False

		Screen:
			name: 'snackbar'
			MDRaisedButton:
				text: "Create simple snackbar"
				size_hint: None, None
				size: 4 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.75}
				opposite_colors: True
				on_release: app.show_example_snackbar('simple')
			MDRaisedButton:
				text: "Create snackbar with button"
				size_hint: None, None
				size: 4 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}
				opposite_colors: True
				on_release: app.show_example_snackbar('button')
			MDRaisedButton:
				text: "Create snackbar with a lot of text and a button"
				size_hint: None, None
				size: 5 * dp(48), dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.25}
				opposite_colors: True
				on_release: app.show_example_snackbar('verylong')

		Screen:
			name: 'textfields'
			ScrollView:
				BoxLayout:
					orientation: 'vertical'
					size_hint_y: None
					height: dp(1000)
					BoxLayout:
						size_hint_y: None
						height: dp(144)
						padding: dp(48)
						SingleLineTextField:
							id: text_field
							size_hint: 0.8, None
							height: dp(48)
							hint_text: "Write something"
					BoxLayout:
						MDLabel:
							font_style: 'Body1'
							theme_text_color: 'Primary'
							text: "Body1 label"
							halign: 'center'
						MDLabel:
							font_style: 'Body2'
							theme_text_color: 'Primary'
							text: "Body2 label"
							halign: 'center'
					BoxLayout:
						MDLabel:
							font_style: 'Caption'
							theme_text_color: 'Primary'
							text: "Caption label"
							halign: 'center'
						MDLabel:
							font_style: 'Subhead'
							theme_text_color: 'Primary'
							text: "Subhead label"
							halign: 'center'
					BoxLayout:
						MDLabel:
							font_style: 'Title'
							theme_text_color: 'Primary'
							text: "Title label"
							halign: 'center'
						MDLabel:
							font_style: 'Headline'
							theme_text_color: 'Primary'
							text: "Headline label"
							halign: 'center'
					MDLabel:
						font_style: 'Display1'
						theme_text_color: 'Primary'
						text: "Display1 label"
						halign: 'center'
						size_hint_y: None
						height: self.texture_size[1] + dp(4)
					MDLabel:
						font_style: 'Display2'
						theme_text_color: 'Primary'
						text: "Display2 label"
						halign: 'center'
						size_hint_y: None
						height: self.texture_size[1] + dp(4)
					MDLabel:
						font_style: 'Display3'
						theme_text_color: 'Primary'
						text: "Display3 label"
						halign: 'center'
						size_hint_y: None
						height: self.texture_size[1] + dp(4)
					MDLabel:
						font_style: 'Display4'
						theme_text_color: 'Primary'
						text: "Display4 label"
						halign: 'center'
						size_hint_y: None
						height: self.texture_size[1] + dp(4)
					BoxLayout:
						MDLabel:
							font_style: 'Body1'
							theme_text_color: 'Primary'
							text: "Primary color"
							halign: 'center'
						MDLabel:
							font_style: 'Body1'
							theme_text_color: 'Secondary'
							text: "Secondary color"
							halign: 'center'
					BoxLayout:
						MDLabel:
							font_style: 'Body1'
							theme_text_color: 'Hint'
							text: "Hint color"
							halign: 'center'
						MDLabel:
							font_style: 'Body1'
							theme_text_color: 'Error'
							text: "Error color"
							halign: 'center'
					MDLabel:
						font_style: 'Body1'
						theme_text_color: 'Custom'
						text_color: (0,1,0,.4)
						text: "Custom"
						halign: 'center'

		Screen:
			name: 'theming'
			BoxLayout:
				orientation: 'vertical'
				size_hint_y: None
				height: dp(80)
				center_y: self.parent.center_y
				MDRaisedButton:
					size_hint: None, None
					size: 3 * dp(48), dp(48)
					center_x: self.parent.center_x
					text: 'Switch theme style'
					on_release: app.theme_cls.theme_style = 'Dark' if app.theme_cls.theme_style == 'Light' else 'Light'
					opposite_colors: True
					pos_hint: {'center_x': 0.5}
				MDLabel:
					text: "Current: " + app.theme_cls.theme_style
					theme_text_color: 'Primary'
					pos_hint: {'center_x': 0.5}
					halign: 'center'

		Screen:
			name: 'toolbar'
			Toolbar:
				title: "Simple toolbar"
				pos_hint: {'center_x': 0.5, 'center_y': 0.38}
				background_color: get_color_from_hex(colors['Teal']['500'])
			Toolbar:
				title: "Toolbar with right buttons"
				pos_hint: {'center_x': 0.5, 'center_y': 0.25}
				background_color: get_color_from_hex(colors['Amber']['700'])
				right_action_items: [['md-content-copy', lambda x: None]]
			Toolbar:
				title: "Toolbar with left and right buttons"
				pos_hint: {'center_x': 0.5, 'center_y': 0.12}
				background_color: get_color_from_hex(colors['DeepPurple']['A400'])
				left_action_items: [['md-arrow-back', lambda x: None]]
				right_action_items: [['md-https', lambda x: None], \
					['md-videocam', lambda x: None], \
					['md-play-arrow', lambda x: None]]

	NavigationDrawer:
		id: nav_drawer
		size_hint_y: None
		height: root.height - toolbar.height
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Bottom sheets"
			on_release: scr_mngr.current = 'bottomsheet'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Buttons"
			on_release: scr_mngr.current = 'button'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Cards"
			on_release: scr_mngr.current = 'card'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Dialogs"
			on_release: scr_mngr.current = 'dialog'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Lists"
			on_release: scr_mngr.current = 'list'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Menus"
			on_release: scr_mngr.current = 'menu'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Progress & activity"
			on_release: scr_mngr.current = 'progress'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Selection controls"
			on_release: scr_mngr.current = 'selectioncontrols'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Snackbars"
			on_release: scr_mngr.current = 'snackbar'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Text fields"
			on_release: scr_mngr.current = 'textfields'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Themes"
			on_release: scr_mngr.current = 'theming'
		NavigationDrawerIconButton:
			icon: 'md-lens'
			text: "Toolbars"
			on_release: scr_mngr.current = 'toolbar'
'''


class KitchenSink(App):
	theme_cls = ThemeManager()

	menu_items = [
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
	]

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		# self.theme_cls.theme_style = 'Dark'

		main_widget.ids.text_field.bind(
				on_text_validate=self.set_error_message,
				on_focus=self.set_error_message)
		return main_widget

	def show_example_snackbar(self, type):
		if type == 'simple':
			Snackbar.make("This is a snackbar!")
		elif type == 'button':
			Snackbar.make("This is a snackbar", button_text="with a button!",
			              button_callback=lambda *args: 2)
		elif type == 'verylong':
			Snackbar.make("This is a very very very very very very very long "
			              "snackbar!",
			              button_text="Hello world")

	def show_example_dialog(self):
		content = MDLabel(font_style='Body1',
		                  theme_text_color='Secondary',
		                  text="This is a dialog with a title and some text. That's pretty awesome right!",
		                  valign='top')

		content.bind(size=content.setter('text_size'))
		self.dialog = MDDialog(title="This is a test dialog",
		                       content=content,
		                       size_hint=(.8, None),
		                       height=dp(200),
		                       auto_dismiss=False)

		self.dialog.add_action_button("Dismiss",
		                              action=lambda
			                              *x: self.dialog.dismiss())
		self.dialog.open()

	def theme_swap(self):
		self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'

	def show_example_bottom_sheet(self):
		bs = MDListBottomSheet()
		bs.add_item("Here's an item with text only", lambda x: x)
		bs.add_item("Here's an item with an icon", lambda x: x,
		            icon='md-cast')
		bs.add_item("Here's another!", lambda x: x, icon='md-nfc')
		bs.open()

	def show_example_grid_bottom_sheet(self):
		bs = MDGridBottomSheet()
		bs.add_item("Facebook", lambda x: x,
		            icon_src='./assets/facebook-box.png')
		bs.add_item("YouTube", lambda x: x,
		            icon_src='./assets/youtube-play.png')
		bs.add_item("Twitter", lambda x: x,
		            icon_src='./assets/twitter.png')
		bs.add_item("Da Cloud", lambda x: x,
		            icon_src='./assets/cloud-upload.png')
		bs.add_item("Camera", lambda x: x,
		            icon_src='./assets/camera.png')
		bs.open()

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


class AvatarSampleWidget(ILeftBody, Image):
	pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
	pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
	pass


if __name__ == '__main__':
	KitchenSink().run()
