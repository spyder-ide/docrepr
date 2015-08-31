# -*- coding: utf-8 -*

"""
View object documentation HTML in a separate GUI window.

Requires PyQt4 or PySide. Original code by
anatoly techtonik <techtonik@gmail.com> is placed in
public domain.

[ ] position window at the center of the screen
    (right now it is middle bottom)
[ ] implement lazy loading for PyQt4/PySide
[ ] remove external dependency on
    IPython.core.oinspect.Inspector
"""


import sys

try:
    from PySide import QtGui, QtWebKit
except ImportError:
    try:
        from PyQt4 import  QtGui, QtWebKit
    except ImportError:
        sys.stderr.write("WebView requires PySide or PyQt4 for GUI window")

try:
    from IPython.core.oinspect import Inspector
except ImportError:
        sys.stderr.write("WebView requires IPython for dumping object info")
    
from .sphinxify import rich_repr, sphinxify


def show_window(url):
    app = QtGui.QApplication([])

    view = QtWebKit.QWebView()
    view.load(url)
    view.show()

    app.exec_()

def webview(obj, oname=''):
    """ Render in tmp and show from tmp """
    oinfo = Inspector().info(obj, oname)

    #from pprint import pprint
    #pprint(oinfo)

    path = rich_repr(oinfo)
    #print path
    #print sphinxify(oinfo['docstring'])
    show_window('file:///' + path.replace('\\', '/'))
