"""
Molecule manipulations.
"""

from .measure import calculate_distance

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """Find the bonds in a molecule (set of coordinates) based on distance criteria.

    The pairwise distance between atoms is computed. If it is in the range 
    `min_bond` to `max_bond`, the atoms are counted as bonded.

    Parameters
    ----------
    coordinates : ndarray
        The coordinates of the atoms.
    max_bond : float (optional)
        The maximum distance for two atoms to be considered bonded. Default is 1.5.
    min_bond : float (optional)
        The minimum distance for two atoms to be considered bonded. Default is 0.

    Returns
    -------
    bonds : dict
        A dictionary where the keys are tuples of the bonded atom indicies, and the
        associated values are the bond lengths.

    """

    if min_bond < 0:
        raise ValueError(F"{min_bond} was entered. Minimum bond length\
             cannot be less than zero.")

    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds