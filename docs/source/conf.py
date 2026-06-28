# Configuration file for the Sphinx documentation builder.

# -- Project information
from sphinx_rtd_theme import __version__ as theme_version
from sphinx_rtd_theme import __version_full__ as theme_version_full
from sphinx.locale import _

project = 'Speedbock-Docs'
version=theme_version
release=theme_version_full
copyright = '2026, Speedbock Technologies'
author = 'Alex Degallaix'
language='en'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_rtd_dark_mode',
    'sphinx_favicon'
]
default_dark_mode = False

source_suffixe = '.rst'
gettext_compact = False


favicons = [
    'speedbock-16x16.png',
    'speedbock-32x32.png',
    'speedbock.svg'
]
 
html_favicon = 'speedbock.ico'


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_theme_options = {
    'prev_next_buttons_location':'bottom',
    'version_selector': True,
    'flyout_display': 'hidden',
    'logo_only': False,
    'version_selector': False,
    
    # Table of content options
    'collapse_navigation':True,
    'sticky_navigation': True,
    'titles_only': False
}

html_logo = 'speedbocktech-logo.png'


# -- Options for EPUB output
epub_show_urls = 'footnote'


