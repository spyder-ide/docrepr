# -*- coding: utf-8 -*-

"""
Utilities
"""

import locale
import sys

PY2 = sys.version_info[0] == 2
PREFERRED_ENCODING = locale.getpreferredencoding()

#==============================================================================
# Python 3 compatibility functions
#==============================================================================
def is_binary_string(obj):
    """Return True if `obj` is a binary string, False if it is anything else"""
    if PY2:
        # Python 2
        return isinstance(obj, str)
    else:
        # Python 3
        return isinstance(obj, bytes)


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
    if is_binary_string(string):
        try:
            unic = string.decode(FS_ENCODING)
        except (UnicodeError, TypeError):
            pass
        else:
            return unic
    return string
