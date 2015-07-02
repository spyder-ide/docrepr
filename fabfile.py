# -*- coding: utf-8 -*

"""
Simple fabric file to test oinspect output
"""

# Stdlib imports
import webbrowser

# Local imports
import oinspect as oi
import oinspect.sphinxify as spxy


def _show_page(url):
    webbrowser.open_new_tab(url)


def test_basic():
    """Test with an empty context"""
    docstring = 'A test'
    url = spxy.doc_repr(docstring, spxy.generate_context())
    _show_page(url)


def test_math():
    """Test a docstring with Latex on it"""
    docstring = 'This is some math :math:`a^2 = b^2 + c^2`'
    url = spxy.doc_repr(docstring, spxy.generate_context())
    _show_page(url)


def test_no_render_math():
    """Test a docstring with Latex on it but without rendering it"""
    docstring = 'This is a rational number :math:`\\frac{x}{y}`'
    oi.options['render_math'] = False
    url = spxy.doc_repr(docstring, spxy.generate_context())
    _show_page(url)


def test_numpy_sin():
    """Test for numpy.sin docstring"""
    import numpy as np
    docstring = np.sin.__doc__
    url = spxy.doc_repr(docstring, spxy.generate_context(name='sin'))
    _show_page(url)


def test_collapse():
    """Test the collapse option"""
    import numpy as np
    docstring = np.sin.__doc__
    oi.options['collapse_sections'] = True
    url = spxy.doc_repr(docstring, spxy.generate_context(name='sin'))
    _show_page(url)


def test_outline():
    """Test the outline option"""
    import numpy as np
    docstring = np.sin.__doc__
    oi.options['outline'] = True
    url = spxy.doc_repr(docstring, spxy.generate_context(name='sin'))
    _show_page(url)


def test_plot():
    """Test the outline option"""
    docstring = """
.. plot::

   >>> import matplotlib.pyplot as plt
   >>> plt.plot([1,2,3], [4,5,6])
"""
    url = spxy.doc_repr(docstring, spxy.generate_context())
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
