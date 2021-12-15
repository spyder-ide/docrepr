from warnings import warn

warn(
    "docrepr.sphinxext.plot_directive is deprecated and will eventually be "
    "removed; please use matplotlib.sphinxext.plot_directive instead",
    DeprecationWarning,
)

from matplotlib.sphinxext.plot_directive import *
