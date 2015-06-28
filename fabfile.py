# -*- coding: utf-8 -*

"""
Simple fabric file to test oinspect output
"""

from __future__ import print_function

import webbrowser

import oinspect.sphinxify as oi

def _show_page(content, fname):
    with open(fname, 'w') as f:
        f.write(content)
    webbrowser.open_new_tab(fname)

def test_basic():
    """Test with an empty context"""
    docstring = 'A test'
    content = oi.sphinxify(docstring, oi.generate_context())
    _show_page(content, '/tmp/test_basic.html')

def test_math():
    """Test a docstring with Latex on it"""
    docstring = 'This is a rational number :math:`\\frac{x}{y}`'
    content = oi.sphinxify(docstring, oi.generate_context())
    _show_page(content, '/tmp/test_math.html')

def run_all():
    """Run all tests"""
    test_basic()
