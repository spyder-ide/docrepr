import docrepr                                # Set module options
from docrepr import sphinxify                 # html generator
from IPython.core.oinspect import Inspector   # oinfo generator

import numpy as np
import math

oinfo = Inspector().info(math.sin or np.sin)
oinfo['name'] = 'sin'
url = sphinxify.rich_repr(oinfo)
print('file://' + url)