import numpy as np
import pytest
from rdkit import Chem

from chemprop.data import MoleculeDataset, MoleculeDatapoint
from chemprop.featurizers import SimpleMoleculeMolGraphFeaturizer


@pytest.fixture(params=[1, 5, 10])
def smis(smis, request):
    return smis.sample(request.param).to_list()


@pytest.fixture
def targets(smis):
    return np.random.rand(len(smis), 1)


@pytest.fixture
def mols(smis):
    return [Chem.MolFromSmiles(smi) for smi in smis]


@pytest.fixture
def V_fs(mols):
    return [np.random.rand(mol.GetNumAtoms(), 2) for mol in mols]


@pytest.fixture
def E_fs(mols):
    return [np.random.rand(mol.GetNumBonds(), 2) for mol in mols]


@pytest.fixture
def V_ds(mols):
    return [np.random.rand(mol.GetNumAtoms(), 2) for mol in mols]


@pytest.fixture
def X_f(mols):
    return [np.random.rand(1, 2) for _ in mols]


@pytest.fixture
def data(request):
    mols, targets, X_f, V_fs, E_fs, V_ds = request.param
    return [
        MoleculeDatapoint(mol=mol, y=target, x_f=x_f, V_f=V_f, E_f=E_f, V_d=V_d)
        for mol, target, x_f, V_f, E_f, V_d in zip(mols, targets, X_f, V_fs, E_fs, V_ds)
    ]


pytestmark = pytest.mark.parametrize(
    "data",
    [(mols, targets, None, None, None, None), (mols, targets, X_f, V_fs, E_fs, V_ds)],
    indirect=True,
)


@pytest.fixture
def dataset(data):
    return MoleculeDataset(data, SimpleMoleculeMolGraphFeaturizer())


def test_none():
    with pytest.raises(ValueError):
        MoleculeDataset(None, SimpleMoleculeMolGraphFeaturizer())


def test_empty():
    """TODO"""


def test_len(data, dataset):
    assert len(data) == len(dataset)


def test_smis(dataset, smis):
    assert smis == dataset.smiles


def test_targets(dataset, targets):
    np.testing.assert_array_equal(dataset.Y, targets)


def test_set_targets_too_short(dataset):
    with pytest.raises(ValueError):
        dataset.Y = np.random.rand(len(dataset) // 2, 1)


def test_num_tasks(dataset, targets):
    assert dataset.t == targets.shape[1]


def test_aux_nones(dataset: MoleculeDataset):
    np.testing.assert_array_equal(dataset.X_f, None)
    np.testing.assert_array_equal(dataset.X_f, None)
    np.testing.assert_array_equal(dataset.V_fs, None)
    np.testing.assert_array_equal(dataset.E_fs, None)
    np.testing.assert_array_equal(dataset.gt_mask, None)
    np.testing.assert_array_equal(dataset.lt_mask, None)
    assert dataset.d_vd == 0
    assert dataset.d_vf == 0
    assert dataset.d_ef == 0


def test_normalize_targets(dataset):
    scaler = dataset.normalize_targets()
    np.testing.assert_array_equal(dataset.Y, (dataset.Y - np.mean(dataset)) / np.std(dataset.Y))
    np.testing.assert_array_equal(scaler.loc_, np.mean(dataset.Y))
    np.testing.assert_array_equal(scaler.scale_, np.std(dataset.Y))


def test_normalize_inputs(dataset):
    for name in ["X_f", "V_fs", "E_fs", "V_ds"]:
        scaler = dataset.normalize_inputs(name)
        np.testing.assert_array_equal(
            getattr(dataset, name),
            (getattr(dataset, name) - np.mean(dataset)) / np.std(getattr(dataset, name)),
        )
        np.testing.assert_array_equal(scaler.loc_, np.mean(getattr(dataset, name)))
        np.testing.assert_array_equal(scaler.scale_, np.std(getattr(dataset, name)))
