"""Setup for Pytest."""

# Standard library imports
import warnings
import webbrowser

# Third party imports
import pytest


# ---- Constants

OPEN_BROWSER_OPTION = '--open-browser'


# ---- Pytest hooks

def pytest_addoption(parser):
    """Add an option to open the user's web browser with HTML test output."""
    parser.addoption(
        OPEN_BROWSER_OPTION,
        action='store_true',
        default=False,
        help='For tests that generate HTML output, open it in a web browser',
    )


# ---- Fixtures

@pytest.fixture
def open_browser(request):
    """Show the passed URL in the user's web browser if passed."""
    def _open_browser(url):
        if request.config.getoption(OPEN_BROWSER_OPTION):
            warnings.filterwarnings(
                'ignore', category=ResourceWarning, module='subprocess.*')

            webbrowser.open_new_tab(url)
    return _open_browser
