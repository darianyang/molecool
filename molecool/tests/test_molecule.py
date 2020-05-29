"""
Unit and regression test for the molecule module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import numpy as np
import sys

"""
If you would like to be able to use your tests across all test modules, 
you put the fixtures in a file called conftest.py. 
"""

# pytest can call function for us with fixtures
# can adjust to use across multiple test modules
# scope module allows fixture to be ran once for all functions
# @pytest.fixture will call for each test, can be costly
@pytest.fixture(scope="module")
def methane_molecule():

    symbols = ['C', 'H', 'H', 'H', 'H']
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    return symbols, coordinates

@pytest.mark.skip
def test_move_methane(methane_molecule):
    
    symbols, coordinates = methane_molecule

    coordinates[0] += 5

def test_build_bond_list(methane_molecule):

    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4

def test_build_bond_failure(methane_molecule):

    symbols, coordinates = methane_molecule

    with pytest.raises(ValueError):
        bonds = molecool.build_bond_list(coordinates, min_bond=-1)

# pass pre-defined fixture as an arg into test funct
def test_molecular_mass(methane_molecule):
    
    symbols, coordinates = methane_molecule

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

    
