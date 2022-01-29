# Copyright (c) 2013- The Spyder Development Team and Docrepr Contributors
#
# Distributed under the terms of the BSD BSD 3-Clause License

"""Simple tests of docrepr's output."""

# Standard library imports
import copy
import subprocess
import sys
import tempfile
from pathlib import Path

# Third party imports
import numpy as np
import pytest
from IPython.core.oinspect import Inspector, object_info

# Local imports
import docrepr
import docrepr.sphinxify


# ---- Test data

# A sample function to test
def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise ValueError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    if 'spam' in kind:
        return ['spam', 'spam', 'eggs', 'spam']
    return ['eggs', 'bacon', 'spam']


# A sample class to test
class SpamCans:
    """
    Cans of spam.

    :param n_cans: Number of cans of spam.
    :type n_cans: int
    :raise ValueError: If spam is negative.

    """

    def __init__(self, n_cans=1):
        """Spam init."""
        if n_cans < 0:
            raise ValueError('Spam must be non-negative!')
        self.n_cans = n_cans

    def eat_one(self):
        """
        Eat one can of spam.

        :raise ValueError: If we're all out of spam.
        :return: The number of cans of spam left.
        :rtype: int

        """
        if self.n_cans <= 0:
            raise ValueError('All out of spam!')
        self.n_cans -= 1
        return self.n_cans


PLOT_DOCSTRING = """
.. plot::

   >>> import matplotlib.pyplot as plt
   >>> plt.plot([1,2,3], [4,5,6])
"""

# Test cases
TEST_CASES = {
    'empty_oinfo': {
        'obj': None,
        'oinfo': {},
        'options': {},
        },
    'basic': {
        'obj': None,
        'oinfo': {
            'name': 'Foo',
            'docstring': 'A test',
            'type_name': 'Function',
            },
        'options': {},
        },
    'function_nosphinx_python_docs': {
        'obj': subprocess.run,
        'oinfo': {'name': 'run'},
        'options': {},
        },
    'class_nosphinx_python_docs': {
        'obj': tempfile.TemporaryDirectory,
        'oinfo': {'name': 'TemporaryDirectory'},
        'options': {},
        },
    'method_nosphinx_thirdparty': {
        'obj': Inspector().info,
        'oinfo': {'name': 'Inspector.info'},
        'options': {},
        },
    'function_sphinx': {
        'obj': get_random_ingredients,
        'oinfo': {'name': 'get_random_ingredients'},
        'options': {},
        },
    'class_sphinx': {
        'obj': SpamCans,
        'oinfo': {'name': 'SpamCans'},
        'options': {},
        },
    'method_sphinx': {
        'obj': SpamCans().eat_one,
        'oinfo': {'name': 'SpamCans.eat_one'},
        'options': {},
        },
    'render_math': {
        'obj': None,
        'oinfo': {
            'name': 'Foo',
            'docstring': 'This is some math :math:`a^2 = b^2 + c^2`',
            },
        'options': {},
        },
    'no_render_math': {
        'obj': None,
        'oinfo': {
            'name': 'Foo',
            'docstring': 'This is a rational number :math:`\\frac{x}{y}`',
            },
        'options': {'render_math': False},
        },
    'numpy_module': {
        'obj': np,
        'oinfo': {'name': 'NumPy'},
        'options': {},
        },
    'numpy_sin': {
        'obj': np.sin,
        'oinfo': {'name': 'sin'},
        'options': {},
        },
    'collapse': {
        'obj': np.sin,
        'oinfo': {'name': 'sin'},
        'options': {'collapse_sections': True},
        },
    'outline': {
        'obj': np.sin,
        'oinfo': {'name': 'sin'},
        'options': {'outline': True},
        },
    'plot': {
        'obj': None,
        'oinfo': {
            'name': 'Foo',
            'docstring': PLOT_DOCSTRING
            },
        'options': {},
        },
    'no_docstring': {
        'obj': None,
        'oinfo': {'docstring': '<no docstring>'},
        'options': {},
        },
    }


# ---- Helper functions

def _test_cases_to_params(test_cases):
    return [
        (test_id, *test_case.values())
        for test_id, test_case in test_cases.items()
    ]


# ---- Fixtures

@pytest.fixture(name='build_oinfo')
def fixture_build_oinfo():
    """Generate object information for tests."""
    def _build_oinfo(obj=None, **oinfo_data):
        if obj is not None:
            oinfo = Inspector().info(obj)
        else:
            oinfo = object_info()
        oinfo = {**oinfo, **oinfo_data}
        return oinfo
    return _build_oinfo


@pytest.fixture(name='set_docrepr_options')
def fixture_set_docrepr_options():
    """Set docrepr's rendering options and restore them after."""
    default_options = copy.deepcopy(docrepr.options)

    def _set_docrepr_options(**docrepr_options):
        docrepr.options.update(docrepr_options)

    yield _set_docrepr_options
    docrepr.options.clear()
    docrepr.options.update(default_options)


# ---- Tests

@pytest.mark.asyncio
@pytest.mark.parametrize(
    ('test_id', 'obj', 'oinfo_data', 'docrepr_options'),
    _test_cases_to_params(TEST_CASES),
    ids=list(TEST_CASES.keys()),
    )
async def test_sphinxify(
        build_oinfo, set_docrepr_options, open_browser, compare_screenshots,
        test_id, obj, oinfo_data, docrepr_options,
        ):
    """Test the operation of the Sphinxify module on various docstrings."""
    if (oinfo_data.get('docstring', None) == PLOT_DOCSTRING
            and sys.version_info.major == 3
            and sys.version_info.minor == 6
            and sys.platform.startswith('win')):
        pytest.skip(
            'Plot fails on Py3.6 on Windows; older version of Matplotlib?')

    oinfo = build_oinfo(obj, **oinfo_data)
    set_docrepr_options(**docrepr_options)

    url = docrepr.sphinxify.rich_repr(oinfo)

    output_file = Path(url)
    assert output_file.is_file()
    assert output_file.suffix == '.html'
    assert output_file.stat().st_size > 512
    file_text = output_file.read_text(encoding='utf-8', errors='strict')
    assert len(file_text) > 512

    await compare_screenshots(test_id, url)
    open_browser(url)
