# pycupti.py
# Wrapper for CUDA's CUPTI library.
#
# Author: Sreepathi Pai <sreepai@ices.utexas.edu> 
#
# Year: 2016
#
# Includes contents of the file cupti.h and subject to the same copyright license

from __future__ import division
from .types import *
from .constants import *

try:
    from .api import *
except OSError as e:
    # TODO: check for actual failure of libcupti loading (which is okay) and other errors...
    pass
