"""
molecool
A python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.
"""

# Add imports here (.) is look in same directory
# import everything = *
from .functions import *


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
