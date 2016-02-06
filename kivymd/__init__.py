# -*- coding: utf-8 -*-
import os

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, "fonts/")
images_path = os.path.join(path, 'images/')

migration_msg = '''
#############################################
#                                           #
# KivyMD has moved to GitLab, this version  #
# has been deprecated.                      #
#                                           #
# Find the new repository at:               #
# https://gitlab.com/kivymd/KivyMD          #
#                                           #
# Reasoning for migration found at old repo #
#                                           #
#############################################
'''

class KivyMDHasMovedToGitLab(Exception):
	pass

raise KivyMDHasMovedToGitLab(migration_msg)
