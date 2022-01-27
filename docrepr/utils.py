"""Utilities (adapted from Spyder source code)."""

# Standard library modules
import locale
import shutil
import sys
from pathlib import Path

PREFERRED_ENCODING = locale.getpreferredencoding()


#==============================================================================
# Encoding functons
#==============================================================================

def getfilesystemencoding():
    """Query filesystem for encoding used to encode filenames & env vars."""
    encoding = sys.getfilesystemencoding()
    if encoding is None:
        # Must be Linux or Unix and nl_langinfo(CODESET) failed.
        encoding = PREFERRED_ENCODING
    return encoding


FS_ENCODING = getfilesystemencoding()


def to_unicode_from_fs(string):
    """Return a unicode version of string decoded using the fs encoding."""
    if isinstance(string, bytes):
        try:
            unic = string.decode(FS_ENCODING)
        except (UnicodeError, TypeError):
            pass
        else:
            return unic
    return string


#==============================================================================
# Filesystem functons
#==============================================================================

def merge_directories(source, destination):
    """Merge a source into a dest dir; compat shim for Python <3.8."""
    try:
        shutil.copytree(source, destination, dirs_exist_ok=True)
    except TypeError:
        pass
    else:
        return
    source = Path(source)
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        source_item = item.resolve()
        destination_item = (destination / item.relative_to(source)).resolve()
        if source_item.is_dir():
            merge_directories(source_item, destination_item)
        else:
            if not destination_item.exists():
                shutil.copy2(source_item, destination_item)
