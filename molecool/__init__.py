"""
molecool
A python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.
"""

# Add imports: here (.) is look in same directory
# import everything = * : bad practice since imports libraries like np
from .functions import *
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .measure import calculate_angle, calculate_distance
from .atom_data import atom_colors, atomic_weights
from .io import open_pdb, open_xyz, write_xyz

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
