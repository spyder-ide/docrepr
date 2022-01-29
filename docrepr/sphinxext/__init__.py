# Copyright (c) 2013- The Spyder Development Team and Docrepr Contributors
#
# Distributed under the terms of the BSD BSD 3-Clause License

"""Backward compatibility shim  for ``matplotlib.sphinxext.plot_directive``."""

from warnings import warn

warn(
    "docrepr.sphinxext.plot_directive is deprecated and will eventually be "
    "removed; please use matplotlib.sphinxext.plot_directive instead",
    DeprecationWarning,
)

from matplotlib.sphinxext.plot_directive import *
