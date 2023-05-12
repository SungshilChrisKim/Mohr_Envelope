# /////////////////////////////////////////////////////////////// #
# Python Script initially created on 2022-01-08
# Compiled by Aly @ Grasselli Geomechanics Group, UofT, 2022
# Created using PyCharm
# /////////////////////////////////////////////////////////////// #
import sys


# Check python compatibility before proceeding
try:
    # version_flag = sys.version_info >= (3, 10)
    assert ((3, 9, 20) >= sys.version_info >= (3, 5))
    # assert (sys.version_info >= (3, 10), 'error!')
    # print("Python Version: %s" % sys.version.split('\n')[0])
except AssertionError:
    print("Error msg: Tested Python Version = 3.5+ upto 3.9.13")
    print("Current Python Version: %s" % sys.version.split('\n')[0])
    sys.exit()

# Load Classes
from .mohr import (
    Read,
    ReadDF,
    Visualize,
    getEnvelope,
)

# Load Functions
from .mohr import (
    load_df,
    read_csv
)
