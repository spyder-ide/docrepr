"""Utilities (adapted from Spyder source code)."""

import locale
import sys

PREFERRED_ENCODING = locale.getpreferredencoding()

#==============================================================================
# Encoding functons
#==============================================================================
def getfilesystemencoding():
    """
    Query the filesystem for the encoding used to encode filenames
    and environment variables.
    """
    encoding = sys.getfilesystemencoding()
    if encoding is None:
        # Must be Linux or Unix and nl_langinfo(CODESET) failed.
        encoding = PREFERRED_ENCODING
    return encoding


FS_ENCODING = getfilesystemencoding()


def to_unicode_from_fs(string):
    """
    Return a unicode version of string decoded using the file system encoding.
    """
    if isinstance(string, bytes):
        try:
            unic = string.decode(FS_ENCODING)
        except (UnicodeError, TypeError):
            pass
        else:
            return unic
    return string
