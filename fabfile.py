# -*- coding: utf-8 -*

"""
Simple fabric file to test oinspect output
"""

from __future__ import print_function

import webbrowser

import oinspect.sphinxify as oi

def test_basic():
    """Test with an empty context"""
    docstring = 'A test'
    content = oi.sphinxify(docstring, oi.generate_context())
    page_name = '/tmp/test_basic.html'
    with open(page_name, 'w') as f:
        f.write(content)
    webbrowser.open_new_tab(page_name)

def run_all():
    """Run all tests"""
    test_basic()
