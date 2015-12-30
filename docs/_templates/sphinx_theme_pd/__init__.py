import os


def get_html_theme_path():
    theme_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return theme_dir
