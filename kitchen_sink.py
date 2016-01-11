# -*- coding: utf-8 -*-
import kivymd.snackbar as Snackbar
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MaterialIconButton
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivymd.selectioncontrols import MaterialCheckBox
from kivymd.theming import ThemeManager
from kivymd.dialog import MDDialog

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import NavigationDrawer kivymd.navigationdrawer.NavigationDrawer
#:import MaterialCheckBox kivymd.selectioncontrols.MaterialCheckBox
#:import MaterialSwitch kivymd.selectioncontrols.MaterialSwitch
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

RelativeLayout:
	Toolbar:
		id: toolbar
		title: 'KivyMD Kitchen Sink'
		left_action_items: [['md-menu', lambda x: nav_drawer.toggle()]]
		right_action_items: [['md-content-copy', lambda x: None], \
		['md-more-vert', lambda x: None]]
	ScreenManager:
		id: scr_mngr
		size_hint_y: None
		height: root.height - toolbar.height
		Screen:
			name: 'bottomsheet'
			
		Screen:
			name: 'button'
			MaterialFlatButton:
				id: flat_button
				text: 'MaterialFlatButton'
				pos_hint: {'center_x': 0.3, 'center_y': 0.75}
			MaterialRaisedButton:
				id: raised_button
				text: "Open dialog"
				elevation_normal: 2
				opposite_colors: True
				size_hint: None, None
				size: dp(110), dp(36)
				pos_hint: {'center_x': 0.75, 'center_y': 0.75}
			FloatingActionButton:
				id:					float_act_btn
				icon:				'md-replay'
				size_hint:			None, None
				size:				dp(56), dp(56)
				opposite_colors:	True
				elevation_normal:	8
				pos_hint:			{'center_x': 0.85, 'center_y': 0.1}

		Screen:
			name: 'card'
			MDCard:
				size_hint: None, None
				size: dp(320), dp(180)
				pos_hint: {'center_x': 0.5, 'center_y': 0.5}

		Screen:
			name: 'dialog'

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
			AnchorLayout:
				anchor_x: 'center'
				anchor_y: 'center'
				MaterialRaisedButton:
					size_hint: None, None
					size: 3 * dp(48), dp(48)
					text: 'Open menu'
					on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)

		Screen:
			name: 'progress'
			MaterialCheckBox:
				id:			chkbox
				size_hint:	None, None
				size:		dp(48), dp(48)
				pos_hint:	{'center_x': 0.5, 'center_y': 0.1}
				active: True
			MDSpinner:
				id: spinner
				size_hint: None, None
				size: dp(46), dp(46)
				pos_hint: {'center_x': 0.15, 'center_y': 0.1}
				active: True if chkbox.active else False

		Screen:
			name: 'selectioncontrols'
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

		Screen:
			name: 'snackbar'

		Screen:
			name: 'textfields'
			MDLabel:
				font_style: 'Subhead'
				theme_text_color: 'Primary'
				text: "Determinate"
				halign: 'center'
				pos_hint: {'center_x': 0.5, 'center_y': 0.14}
			SingleLineTextField:
				id: text_field
				size_hint: 0.8, None
				height: dp(48)
				pos_hint: {'center_x': 0.5, 'center_y': 0.85}
				hint_text: "Write something"

		Screen:
			name: 'theming'
			BoxLayout:
				orientation: 'vertical'
				size_hint_y: None
				height: dp(80)
				center_y: self.parent.center_y
				MaterialRaisedButton:
					size_hint: None, None
					size: 3 * dp(48), dp(48)
					center_x: self.parent.center_x
					text: 'Switch theme style'
					on_release: app.theme_cls.theme_style = 'Dark' if app.theme_cls.theme_style == 'Light' else 'Light'
					pos_hint: {'center_x': 0.5}
				MDLabel:
					text: "Current: " + app.theme_cls.theme_style
					theme_text_color: 'Primary'
					pos_hint: {'center_x': 0.5}
					halign: 'center'

		Screen:
			name: 'toolbar'

	NavigationDrawer:
		id: nav_drawer
		bind_to_window: False
		size_hint_y: None
		height: root.height - toolbar.height
		NavigationDrawerCategory:
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
				text: "Progres & activity"
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
	]

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		# self.theme_cls.theme_style = 'Dark'
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
		                              action=lambda *x: self.dialog.dismiss())
		main_widget.ids.raised_button.bind(
				on_release=lambda *x: self.dialog.open())
		main_widget.ids.flat_button.bind(
				on_release=lambda *x: Snackbar.make("This is a snackbar!",
				                                    button_text="Hello world",
				                                    button_callback=lambda
					                                    *args: 2))
		main_widget.ids.li_icon_1.bind(
				on_release=lambda *x: Snackbar.make(
						"This is a very very very very very very very long snackbar!",
						button_text="Hello world"))
		main_widget.ids.li_icon_2.bind(
				on_release=lambda *x: self.show_example_bottom_sheet()
		)
		main_widget.ids.li_icon_3.bind(
				on_release=lambda *x: self.show_example_grid_bottom_sheet()
		)
		main_widget.ids.text_field.bind(
				on_text_validate=self.set_error_message,
				on_focus=self.set_error_message)
		return main_widget

	def theme_swap(self):
		self.theme_cls.theme_style = 'Dark' if self.theme_cls.theme_style == 'Light' else 'Light'

	def show_example_bottom_sheet(self):
		bs = MDListBottomSheet()
		bs.add_item("Here's an item with text only", lambda x: x)
		bs.add_item("Here's an item with an icon", lambda x: x, icon='md-cast')
		bs.add_item("Here's another!", lambda x: x, icon='md-nfc')
		bs.open()

	def show_example_grid_bottom_sheet(self):
		bs = MDGridBottomSheet()
		bs.add_item("Facebook", lambda x: x,
		            icon_src='./assets/facebook-box.png')
		bs.add_item("YouTube", lambda x: x,
		            icon_src='./assets/youtube-play.png')
		bs.add_item("Twitter", lambda x: x, icon_src='./assets/twitter.png')
		bs.add_item("Da Cloud", lambda x: x,
		            icon_src='./assets/cloud-upload.png')
		bs.add_item("Camera", lambda x: x, icon_src='./assets/camera.png')
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


class IconLeftSampleWidget(ILeftBodyTouch, MaterialIconButton):
	pass


class IconRightSampleWidget(IRightBodyTouch, MaterialCheckBox):
	pass


if __name__ == '__main__':
	KitchenSink().run()
