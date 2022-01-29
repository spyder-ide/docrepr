# Docrepr

Docrepr renders Python docstrings to HTML with Sphinx.
It can generate rich and plain representations of docstrings, alongside additional metadata about the object to which the docstring belongs.
It is based on the `sphinxify` module developed by [Tim Dumol](https://github.com/TimDumol) for the Sage Notebook and the `utils.help` module developed by [Carlos Cordoba](https://github.com/ccordoba12) for the Spyder IDE.
See [spyder-ide/docrepr#20](https://github.com/spyder-ide/docrepr/issues/20) for the full history.


## Rationale

For more on the motivation and design behind Docrepr, see this presentation by Carlos Cordoba at SciPy 2015:

[![Towards a Better Documentation System for Scientific Python | SciPy 2015 | Carlos Cordoba ](https://img.youtube.com/vi/q0r7FsDZU9s/0.jpg)](https://www.youtube.com/watch?v=q0r7FsDZU9s)


## Details

The module renders a dictionary as returned by IPython `oinspect` module into a full HTML page (with all assets) from an object's docstring, by using the `rich_repr` function of its `sphinxify` submodule.


## Example of use

```python
import webbrowser

import numpy as np
from IPython.core.oinspect import Inspector   # oinfo generator

import docrepr                                # Set module options
from docrepr import sphinxify                 # html generator

oinfo = Inspector().info(np.sin)
oinfo['name'] = 'sin'
url = sphinxify.rich_repr(oinfo)

webbrowser.open_new_tab(url)
```


## License

This project is distributed under the under the terms of the [BSD 3-Clause License](https://github.com/spyder-ide/docrepr/blob/master/LICENSE.txt).
