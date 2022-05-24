import numpy as np
import pytest
from rdkit import Chem

from chemprop.featurizers.multihot.bond import BondFeaturizer


@pytest.fixture(
    params=list(Chem.MolFromSmiles("Cn1nc(CC(=O)Nc2ccc3oc4ccccc4c3c2)c2ccccc2c1=O").GetBonds())
)
def bond(request):
    return request.param


@pytest.fixture
def bond_types():
    return [1, 2, 3, 12]


@pytest.fixture
def stereo():
    return list(range(6))


@pytest.fixture
def featurizer(bond_types, stereo):
    return BondFeaturizer(bond_types, stereo)


@pytest.fixture
def exp_len(bond_types, stereo):
    return sum([1, len(bond_types), 1, 1, (len(stereo) + 1)])


@pytest.fixture
def bt_bit(bond, bond_types, featurizer):
    bt = bond.GetBondType()
    i_bt = int(bt)

    i = bond_types.index(i_bt) if i_bt in bond_types else -1

    if i == -1:
        return i

    return range(len(featurizer))[featurizer.subfeatures["bond_type"] + i]


@pytest.fixture
def x(featurizer, bond):
    return featurizer(bond)


def test_len(featurizer, exp_len):
    assert len(featurizer) == exp_len


def test_none(featurizer):
    x_e = np.zeros(len(featurizer))
    x_e[0] = 1

    np.testing.assert_array_equal(x_e, featurizer(None))


def test_bt_bit(x, bt_bit):
    assert x[bt_bit] == 1


def test_conj_bit(featurizer, x, bond):
    conj_bit = featurizer.subfeatures["conjugated"]

    assert x[conj_bit] == int(bond.GetIsConjugated())


@pytest.mark.parametrize(
    "mol,X_e_orig",
    [
        (
            Chem.MolFromSmiles("O=C(NCc1ccc(Cn2ccccc2=O)cc1)c1ccccc1CCc1ccccc1"),
            np.array(
                [
                    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                ]
            ),
        )
    ],
)
def test_x_hand_calc(mol, X_e_orig):
    f = BondFeaturizer()

    bonds = list(mol.GetBonds())
    X_e_calc = np.array([f(b) for b in bonds[: len(X_e_orig)]])
    np.testing.assert_array_almost_equal(X_e_calc, X_e_orig)
