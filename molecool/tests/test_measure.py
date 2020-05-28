"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import numpy as np
import sys

@pytest.mark.skip
def test_calculate_distance():
    """
    Test of distance calculation.
    """

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1
    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():
    """
    Test of angle calculation.
    """

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = 90
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_angle == calculated_angle

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert np.array_equal(center_of_mass, expected_center)
