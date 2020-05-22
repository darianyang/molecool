""" 
Functions for measurements and building bond lists.
"""

import numpy as np

# example of numpy style docstring
def calculate_distance(rA, rB):
    """
    Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.
    
    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> rA = np.array([0.0, 0.0, 0.0])
    >>> rB = np.array([0.0, 0.0, 1.0])
    >>> calculate_distance(rA, rB)
    1.0

    """
    # can access doc string with 
        # >>> help(molecool.calculate_distance)
        # >>> molecool.calculate_distance.__doc__
        # >>> print(molecool.calculate_distance.__doc__)

    # This function calculates the distance between two points given as numpy arrays.
    
    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray is False):
        raise TypeError("rA abd rB must be numpy arrays")

    d=(rA-rB)
    dist=np.linalg.norm(d)

    if dist == 0.0:
        raise Exception("Two atoms are located at the same point")

    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle between three points. 
    Answer is given in radians by default, but can be given in degrees
    by setting degrees=True.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
    degrees : True/False

    Returns
    -------
    theta : float
        The angle between three points.

    Examples
    --------
    >>> 

    """
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
