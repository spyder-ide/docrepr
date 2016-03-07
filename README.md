# About

`docrepr` renders Python docstrings in HTML. It is based on the sphinxify module
developed by Tim Dumol for the Sage Notebook and the utils.inspector developed
for ther Spyder IDE.

# Rationale

Video presentation @ SciPy 2015 by Carlos Cordoba:

[![Towards a Better Documentation System for Scientific Python | SciPy 2015 | Carlos Cordoba ](http://img.youtube.com/vi/q0r7FsDZU9s/0.jpg)](http://www.youtube.com/watch?v=q0r7FsDZU9s)

# Details

The module renders a dictionary as returned by IPython `oinspect` module
into a full HTML page (with all assets) from an object's docstring, by
using the `rich_repr` function of its `sphinxify` submodule.

# Example of use

```python
import webbrowser

import docrepr                                # Set module options
from docrepr import sphinxify                 # html generator
from IPython.core.oinspect import Inspector   # oinfo generator

import numpy as np

oinfo = Inspector().info(np.sin)
oinfo['name'] = 'sin'
url = sphinxify.rich_repr(oinfo)

webbrowser.open_new_tab(url)
```

# License

This project is distributed under the under the terms of the Modified BSD
License
