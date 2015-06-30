# -*- coding: utf-8 -*

"""
Process docstrings with Sphinx

AUTHORS:
- Tim Joseph Dumol (2009-09-29): initial version
- The Spyder Development Team: Several changes to make it work with Spyder

Copyright (C) 2009 Tim Dumol <tim@timdumol.com>
Copyright (C) 2013- The Spyder Development Team
Distributed under the terms of the BSD License

Taken from the Sage project (www.sagemath.org).
See here for the original version:
http://doc.sagemath.org/html/en/reference/notebook/sagenb/misc/sphinxify.html
"""

# Stdlib imports
import codecs
import os
import os.path as osp
import shutil
import sys
import tempfile
from xml.sax.saxutils import escape

# 3rd party imports
from docutils.utils import SystemMessage as SystemMessage
from jinja2 import Environment, FileSystemLoader
import sphinx
from sphinx.application import Sphinx

# Local imports
from . import options
from .utils import to_unicode_from_fs, to_binary_string


#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------
CONFDIR_PATH = osp.dirname(__file__)
CSS_PATH = osp.join(CONFDIR_PATH, 'static', 'css')
JS_PATH = osp.join(CONFDIR_PATH, 'js')
JQUERY_PATH = JS_PATH

if os.name == 'nt':
    CACHEDIR = tempfile.gettempdir() + osp.sep + 'spyder'
else:
    username = to_unicode_from_fs(os.environ.get('USER'))
    CACHEDIR = tempfile.gettempdir() + osp.sep + 'oinspect-' + username

#-----------------------------------------------------------------------------
# Utility functions
#-----------------------------------------------------------------------------
def is_sphinx_markup(docstring):
    """Returns whether a string contains Sphinx-style ReST markup."""
    # this could be made much more clever
    return ("`" in docstring or "::" in docstring)


def warning(message):
    """Print a warning message on the rich text view"""
    env = Environment()
    env.loader = FileSystemLoader(osp.join(CONFDIR_PATH, 'templates'))
    warning = env.get_template("warning.html")
    return warning.render(css_path=CSS_PATH, text=message)


def generate_conf(directory):
    """
    Generates a Sphinx configuration file in `directory`.

    Parameters
    ----------
    directory : str
        Base directory to use
    """
    # conf.py file for Sphinx
    conf = osp.join(CONFDIR_PATH, 'conf.py')

    # Docstring layout page (in Jinja):
    layout = osp.join(osp.join(CONFDIR_PATH, 'templates'), 'layout.html')

    os.makedirs(osp.join(directory, 'templates'))
    os.makedirs(osp.join(directory, 'static'))
    shutil.copy(conf, directory)
    shutil.copy(layout, osp.join(directory, 'templates'))
    open(osp.join(directory, '__init__.py'), 'w').write('')
    open(osp.join(directory, 'static', 'empty'), 'w').write('')


def generate_context(name=None, argspec=None, note=None, img_path=''):
    """
    Generate the html_context dictionary for our Sphinx conf file.

    This is a set of variables to be passed to the Jinja template engine and
    that are used to control how the webpage is rendered in connection with
    Sphinx

    Parameters
    ----------
    name : str
        Object's name.
    note : str
        A note describing what type has the function or method being
        introspected
    argspec : str
        Argspec of the the function or method being introspected
    collapse : bool
        Collapse sections

    Returns
    -------
    A dict of strings to be used by Jinja to generate the webpage
    """

    # Default values
    if name is None:
        name = 'foo'
    if argspec is None:
        argspec = '(x, y)'
    if note is None:
        note = 'Function of Bar module'

    if options['local_mathjax']:
        # TODO: Fix local use of MathJax
        MATHJAX_PATH = "file:///" + osp.join(JS_PATH, 'mathjax')
    else:
        MATHJAX_PATH = "https://cdn.mathjax.org/mathjax/latest"

    context = \
    {
      # Arg dependent variables
      'name': name,
      'argspec': argspec,
      'note': note,
      'img_path': img_path,

      # Static variables
      'css_path': CSS_PATH,
      'js_path': JS_PATH,
      'jquery_path': JQUERY_PATH,
      'mathjax_path': MATHJAX_PATH,
      'math_on': 'true' if options['render_math'] else '',
      'platform': sys.platform,
      'collapse': options['collapse_sections'],
      'use_qt4': options['use_qt4'],
      'outline': options['outline']
    }

    return context


def generate_extensions(render_math):
    """Generate list of Sphinx extensions"""
    # We need jsmath to get pretty plain-text latex in docstrings
    extensions = []
    if sphinx.__version__ < "1.1" or not render_math:
        extensions = ['sphinx.ext.jsmath']
    else:
        extensions = ['sphinx.ext.mathjax']

    # For scipy and matplotlib docstrings, which need this extension to
    # be rendered correctly (see Issue 1138)
    extensions.append('sphinx.ext.autosummary')

    # Plots
    try:
        # TODO: Add an option to avoid importing mpl every time
        import matplotlib   # analysis:ignore
        extensions.append('plot_directive')
    except ImportError:
        pass

    return extensions


def sphinxify(docstring, context, buildername='html', temp_confdir=False):
    """
    Runs Sphinx on a docstring and outputs the processed documentation.

    Parameters
    ----------
    docstring : str
        a ReST-formatted docstring

    context : dict
        Variables to be passed to the layout template to control how its
        rendered (through the Sphinx variable *html_context*).

    buildername:  str
        It can be either `html` or `text`.

    Returns
    -------
    An Sphinx-processed string, in either HTML or plain text format, depending
    on the value of `buildername`
    """

    # Create srcdir
    if not osp.isdir(CACHEDIR):
        os.mkdir(CACHEDIR)
    srcdir = tempfile.mkdtemp(dir=CACHEDIR)
    srcdir = to_unicode_from_fs(srcdir)

    # Rst file to sphinxify
    base_name = osp.join(srcdir, 'docstring')
    rst_name = base_name + '.rst'

    # Output file name
    if buildername == 'html':
        suffix = '.html'
    else:
        suffix = '.txt'
    output_name = base_name + suffix

    # This is needed so users can type \\ on latex eqnarray envs inside raw
    # docstrings
    if context['math_on']:
        docstring = docstring.replace('\\\\', '\\\\\\\\')

    # Write docstring to rst_name
    with codecs.open(rst_name, 'w', encoding='utf-8') as rst_file:
        rst_file.write(docstring)

    # Add a class to several characters on the argspec. This way we can
    # highlight them using css, in a similar way to what IPython does.
    # NOTE: Before doing this, we escape common html chars so that they
    # don't interfere with the rest of html present in the page
    argspec = escape(context['argspec'])
    for char in ['=', ',', '(', ')', '*', '**']:
        argspec = argspec.replace(char,
                         '<span class="argspec-highlight">' + char + '</span>')
    context['argspec'] = argspec

    # Create confdir
    if temp_confdir:
        # TODO: This may be inefficient. Find a faster way to do it.
        confdir = tempfile.mkdtemp()
        confdir = to_unicode_from_fs(confdir)
        generate_conf(confdir)
    else:
        confdir = CONFDIR_PATH

    # Get extensions list
    extensions = generate_extensions(options['render_math'])

    # Override conf variables
    confoverrides = {'html_context': context, 'extensions': extensions}

    # Create Sphinx app
    doctreedir = osp.join(srcdir, 'doctrees')
    sphinx_app = Sphinx(srcdir, confdir, srcdir, doctreedir, buildername,
                        confoverrides, status=None, warning=None,
                        freshenv=True, warningiserror=False, tags=None)

    # Run the app
    try:
        sphinx_app.build(None, [rst_name])
    except SystemMessage:
        error_message = "It was not possible to get rich help for this object"
        output = warning(error_message)
        with open(output_name, 'wb') as f:
            f.write(to_binary_string(output, encoding='utf-8'))
        return output_name

    # Some adjustments to the output
    if osp.exists(output_name):
        output = codecs.open(output_name, 'r', encoding='utf-8').read()
        output = output.replace('<pre>', '<pre class="literal-block">')
    else:
        error_message = "It was not possible to get rich help for this object"
        output = warning(error_message)

    # Remove temp confdir
    if temp_confdir:
        shutil.rmtree(confdir, ignore_errors=True)

    # Rewrite output contents after adjustments
    with open(output_name, 'wb') as f:
        f.write(to_binary_string(output, encoding='utf-8'))

    # Return output file name
    return output_name
