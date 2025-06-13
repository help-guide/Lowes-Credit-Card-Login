# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'How to Apply for the Lowe’s Credit Card'
copyright = '2025, Lowe’s'
author = 'Lowe’s'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Apply for the Lowe’s Credit Card – Full Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Lowe’s Credit Card"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Theme (uncomment and install if necessary)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have static assets

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
