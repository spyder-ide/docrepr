# -*- coding: utf-8 -*

"""
Simple fabric file to test oinspect output
"""

# Stdlib imports
import webbrowser

# Local imports
import oinspect as oi
import oinspect.utils as utils
import oinspect.sphinxify as spxy


def _show_page(content, fname):
    with open(fname, 'wb') as f:
        f.write(utils.to_binary_string(content, encoding='utf-8'))
    webbrowser.open_new_tab(fname)


def test_basic():
    """Test with an empty context"""
    docstring = 'A test'
    content = spxy.sphinxify(docstring, spxy.generate_context())
    _show_page(content, '/tmp/test_basic.html')


def test_math():
    """Test a docstring with Latex on it"""
    docstring = 'This is some math :math:`a^2 = b^2 + c^2`'
    content = spxy.sphinxify(docstring, spxy.generate_context())
    _show_page(content, '/tmp/test_math.html')


def test_no_render_math():
    """Test a docstring with Latex on it but without rendering it"""
    docstring = 'This is a rational number :math:`\\frac{x}{y}`'
    oi.options['render_math'] = False
    content = spxy.sphinxify(docstring, spxy.generate_context())
    _show_page(content, '/tmp/test_no_render_math.html')


def test_numpy_sin():
    """Test for numpy.sin docstring"""
    import numpy as np
    docstring = np.sin.__doc__
    content = spxy.sphinxify(docstring, spxy.generate_context(name='sin'))
    _show_page(content, '/tmp/test_np_sin.html')


def test_collapse():
    """Test the collapse option"""
    import numpy as np
    docstring = np.sin.__doc__
    oi.options['collapse_sections'] = True
    content = spxy.sphinxify(docstring, spxy.generate_context(name='sin'))
    _show_page(content, '/tmp/test_collapse.html')


def test_outline():
    """Test the outline option"""
    import numpy as np
    docstring = np.sin.__doc__
    oi.options['outline'] = True
    content = spxy.sphinxify(docstring, spxy.generate_context(name='sin'))
    _show_page(content, '/tmp/test_collapse.html')


def run_all():
    """Run all tests"""
    test_basic()
    test_math()
    test_numpy_sin()
