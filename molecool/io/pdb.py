"""
Functions for manipulating PDB files.
"""

import os
import numpy as np

def open_pdb(f_loc):
    """
    This function reads in a pdb file and returns the atom names and coordinates.

    Parameters
    ----------
    f_loc : string for file location

    Returns
    -------
    sym : list
    coords : ndarray

    Examples
    --------
    >>> open_pdb("/path/to/file")

    """

    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            try:
                # list comprehension: for x in list_object: --> float(x)
                c2 = [float(x) for x in l[30:55].split()]
            except ValueError as e:
                raise ValueError(F"error in pdb file {f_loc} formatting.\n {e}")
            else:
                c.append(c2)
    coords = np.array(c)
    return sym, coords
