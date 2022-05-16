code = """
from numba import jit, njit
import numpy as np
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.filterwarnings("ignore")
"""