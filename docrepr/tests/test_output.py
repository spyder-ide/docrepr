"""Simple tests of docrepr's output."""

# Standard library imports
import copy
import subprocess
from pathlib import Path

# Third party imports
import numpy as np
import pytest
from IPython.core.oinspect import Inspector, object_info

# Local imports
import docrepr
import docrepr.sphinxify as sphinxify


# ---- Test data

LONG_DOCSTRING = """
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
            'argspec': {},
            'docstring': 'A test',
            'type_name': 'Function',
            },
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
            'docstring': LONG_DOCSTRING
            },
        'options': {},
        },
    'python_docs': {
        'obj': subprocess.run,
        'oinfo': {'name': 'run'},
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
    return [tuple(test_case.values()) for test_case in test_cases.values()]


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

@pytest.mark.parametrize(
    ('obj', 'oinfo_data', 'docrepr_options'),
    _test_cases_to_params(TEST_CASES),
    ids=list(TEST_CASES.keys()),
    )
def test_sphinxify(
        build_oinfo, set_docrepr_options, open_browser,
        obj, oinfo_data, docrepr_options,
        ):
    oinfo = build_oinfo(obj, **oinfo_data)
    set_docrepr_options(**docrepr_options)
    url = sphinxify.rich_repr(oinfo)
    output_file = Path(url)
    assert output_file.is_file()
    assert output_file.suffix == '.html'
    assert output_file.stat().st_size > 512
    file_text = output_file.read_text(encoding='utf-8', errors='strict')
    assert len(file_text) > 512
    open_browser(url)
