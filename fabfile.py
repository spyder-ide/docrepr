# -*- coding: utf-8 -*

"""
Simple fabric file to test docrepr output
"""

# Stdlib imports
import webbrowser

# 3rd party imports
from IPython.core.oinspect import Inspector, object_info

# Local imports
import docrepr as dr
import docrepr.sphinxify as spxy


# Main inspector instance
inspector = Inspector()


def _show_page(url):
    webbrowser.open_new_tab(url)


def test_empty_oinfo():
    """Test with totally empty oinfo"""
    oinfo = object_info()
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_basic():
    """Test with an empty context"""
    oinfo = object_info()
    oinfo['name'] = 'Foo'
    oinfo['argspec'] = {}
    oinfo['docstring'] = 'A test'
    oinfo['type_name'] = 'Function'
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_math():
    """Test a docstring with Latex on it"""
    oinfo = object_info()
    oinfo['name'] = 'Foo'
    oinfo['docstring'] = 'This is some math :math:`a^2 = b^2 + c^2`'
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_no_render_math():
    """Test a docstring with Latex on it but without rendering it"""
    oinfo = object_info()
    oinfo['name'] = 'Foo'
    oinfo['docstring'] = 'This is a rational number :math:`\\frac{x}{y}`'
    dr.options['render_math'] = False
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_numpy_sin():
    """Test for numpy.sin docstring"""
    import numpy as np
    oinfo = inspector.info(np.sin)
    oinfo['name'] = 'sin'
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_collapse():
    """Test the collapse option"""
    import numpy as np
    oinfo = inspector.info(np.sin)
    oinfo['name'] = 'sin'
    dr.options['collapse_sections'] = True
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_outline():
    """Test the outline option"""
    import numpy as np
    oinfo = inspector.info(np.sin)
    oinfo['name'] = 'sin'
    dr.options['outline'] = True
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_plot():
    """Test for plots"""
    docstring = """
.. plot::

   >>> import matplotlib.pyplot as plt
   >>> plt.plot([1,2,3], [4,5,6])
"""
    oinfo = object_info()
    oinfo['name'] = 'Foo'
    oinfo['docstring'] = docstring
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_docs_py():
    """Test linking to docs.python.org"""
    import subprocess as sp
    oinfo = inspector.info(sp.Popen)
    oinfo['name'] = 'Popen'
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_no_doc():
    """Test for no docstring"""
    oinfo = object_info()
    oinfo['docstring'] = '<no docstring>'
    url = spxy.rich_repr(oinfo)
    _show_page(url)


def test_all():
    """Run all tests"""
    test_basic()
    test_math()
    test_no_render_math()
    test_numpy_sin()
    test_collapse()
    test_outline()
    test_plot()
