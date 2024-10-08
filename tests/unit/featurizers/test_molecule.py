# flake8: noqa
import numpy as np
import pytest
from rdkit import Chem

from chemprop.featurizers import (
    MorganBinaryFeaturizer,
    MorganCountFeaturizer,
    RDKit2DFeaturizer,
    V1RDKit2DFeaturizer,
    V1RDKit2DNormalizedFeaturizer,
)


@pytest.fixture
def mol():
    return Chem.MolFromSmiles("Fc1cccc(C2(c3nnc(Cc4cccc5ccccc45)o3)CCOCC2)c1")


# fmt: off
@pytest.fixture
def morgan_binary_bits():
    return np.array([[  80,  230,  332,  378,  429,  450,  502,  503,  523,  544,  556,
                      645,  649,  656,  663,  699,  772,  875,  917,  926,  950, 1039,
                     1060, 1087, 1088, 1104, 1136, 1162, 1164, 1199, 1349, 1357, 1380,
                     1405, 1430, 1487, 1510, 1561, 1573, 1597, 1604, 1670, 1742, 1747,
                     1750, 1824, 1855, 1873, 1928]])


@pytest.fixture
def morgan_count_bits():
    return np.array([ 1,  1,  1,  2,  1,  1,  1,  1,  1,  1,  1,  2,  1,  2,  1,  1,  1,
                      1,  1,  4,  2,  2,  1,  2,  4,  1,  1,  2,  2,  2,  1,  1,  7,  1,
                      1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  6,  2,  1, 11,  1])


@pytest.fixture
def morgan_binary_custom():
    return np.array([[ 15,  36,  49,  63,  64,  80, 112, 138, 140, 175, 230, 275, 301,
                     325, 332, 333, 339, 356, 378, 381, 406, 429, 450, 463, 465, 478,
                     486, 502, 503, 517, 523, 524, 537, 544, 549, 554, 556, 573, 579,
                     580, 645, 646, 647, 649, 652, 656, 663, 699, 718, 721, 723, 726,
                     731, 772, 773, 800, 818, 821, 828, 831, 836, 849, 865, 875, 887,
                     894, 904, 917, 926, 950, 951, 989]])


@pytest.fixture
def rdkit_2d_values():
    return np.array([     13.9511,      13.9511,       0.2603,      -0.5096,
                           0.4909,      16.1724,     388.442 ,     367.274 ,
                         388.1587,     146.    ,       0.    ,       0.2267,
                          -0.4239,       0.4239,       0.2267,       0.8966,
                           1.6897,       2.5517,      19.1421,       9.7377,
                           2.4117,      -2.34  ,       2.4051,      -2.3511,
                           5.8532,       0.054 ,       3.2361,       1.5168,
                        1143.0568,      19.6836,      15.9753,      15.9753,
                          14.244 ,       9.8787,       9.8787,       7.5208,
                           7.5208,       5.8214,       5.8214,       4.26  ,
                           4.26  ,      -3.05  , 9626644.372 ,      18.0088,
                           7.4091,       3.3162,     167.8922,       9.154 ,
                           5.8172,       0.    ,      11.7814,       0.    ,
                           0.    ,       0.    ,       4.3904,       0.    ,
                          10.1974,      54.5973,      46.8737,      13.2138,
                          11.8358,      13.5444,      10.7724,       0.    ,
                          10.1974,       0.    ,      24.6775,      13.2138,
                          95.4556,       0.    ,       0.    ,       0.    ,
                           4.3904,       0.    ,       0.    ,      23.4111,
                          16.5727,       5.8172,      35.75  ,      71.1472,
                           0.    ,      10.7724,       0.    ,      48.15  ,
                           5.415 ,       4.3904,       0.    ,       5.8172,
                          44.2577,      11.1269,      16.8388,      12.1327,
                          24.2655,      34.4628,       9.154 ,      25.6895,
                           0.    ,       0.    ,      11.1016,       1.4962,
                           0.851 ,      21.1832,       1.9333,       1.1618,
                           0.    ,       0.25  ,      29.    ,       0.    ,
                           4.    ,       0.    ,       1.    ,       1.    ,
                           3.    ,       1.    ,       4.    ,       4.    ,
                           0.    ,       5.    ,       4.    ,       0.    ,
                           1.    ,       1.    ,       5.    ,       5.0492,
                         108.285 ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       2.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           2.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       3.    ,
                           0.    ,       1.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       1.    ,       0.    ,
                           0.    ,       1.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ])

@pytest.fixture
def v1_rdkit_2d_values():  
    return np.array([      1.5168,    1143.0568,      19.6836,      15.9753,
                          15.9753,      14.244 ,       9.8787,       9.8787,
                           7.5208,       7.5208,       5.8214,       5.8214,
                           4.26  ,       4.26  ,       5.415 ,       4.3904,
                           0.    ,       5.8172,      44.2577,      11.1269,
                          16.8388,      12.1327,      24.2655,      34.4628,
                           9.154 ,     388.1587,       0.8966,       1.6897,
                           2.5517,       0.25  ,      -3.05  ,      29.    ,
                         367.274 , 9626644.372 ,      18.0088,       7.4091,
                           3.3162,     167.8922,      13.9511,       0.4239,
                          13.9511,       0.2267,       0.2603,       0.2267,
                          -0.5096,      -0.4239,       5.0492,     108.285 ,
                         388.442 ,       0.    ,       4.    ,       0.    ,
                           1.    ,       1.    ,       3.    ,       1.    ,
                           4.    ,       4.    ,       0.    ,       5.    ,
                           0.    ,       4.    ,       0.    ,       1.    ,
                           1.    ,     146.    ,       9.154 ,       5.8172,
                           0.    ,      11.7814,       0.    ,       0.    ,
                           0.    ,       4.3904,       0.    ,      10.1974,
                          54.5973,      46.8737,      13.2138,      11.8358,
                           5.    ,      13.5444,      10.7724,       0.    ,
                          10.1974,       0.    ,      24.6775,      13.2138,
                          95.4556,       0.    ,       0.    ,       0.    ,
                           4.3904,       0.    ,       0.    ,      23.4111,
                          16.5727,       5.8172,      35.75  ,      71.1472,
                           0.    ,      10.7724,       0.    ,      48.15  ,
                          25.6895,       0.    ,       0.    ,      11.1016,
                           1.4962,       0.851 ,      21.1832,       1.9333,
                           1.1618,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       2.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       2.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           3.    ,       0.    ,       1.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       1.    ,
                           0.    ,       0.    ,       1.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.    ,
                           0.    ,       0.    ,       0.    ,       0.4909])

@pytest.fixture
def v1_rdkit_2d_normalized_values():
    return np.array([0.2662, 0.6887, 0.5077, 0.5362, 0.4843, 0.6014, 0.6126, 0.534 ,
                     0.6197, 0.513 , 0.7176, 0.6135, 0.7476, 0.6436, 0.5736, 0.2421,
                     0.    , 0.2162, 0.9261, 0.2905, 0.8332, 0.5472, 0.6221, 0.8157,
                     0.5639, 0.4934, 0.1407, 0.2732, 0.553 , 0.3169, 0.3848, 0.5742,
                     0.4977, 1.    , 0.4275, 0.3974, 0.4283, 0.5421, 0.8529, 0.349 ,
                     0.8529, 0.2728, 0.8296, 0.2614, 0.4263, 0.6376, 0.8529, 0.5321,
                     0.4905, 0.0613, 0.1937, 0.    , 0.9187, 0.5   , 0.964 , 0.865 ,
                     0.9176, 0.3071, 0.0553, 0.2075, 0.    , 0.2143, 0.    , 0.98  ,
                     0.8807, 0.5194, 0.3119, 0.4701, 0.    , 0.9161, 0.    , 0.    ,
                     0.06  , 0.6132, 0.    , 1.    , 0.8269, 0.6454, 0.2879, 0.4656,
                     0.8852, 0.5202, 0.218 , 0.1671, 0.4275, 0.    , 0.5073, 0.4523,
                     0.9257, 0.0001, 0.    , 0.0373, 0.9759, 0.    , 0.    , 0.2569,
                     0.6995, 0.9386, 0.6704, 0.8781, 0.    , 0.9855, 0.0001, 0.1612,
                     0.0001, 0.5   , 0.3847, 0.0001, 0.0001, 0.9999, 0.0001, 0.9987,
                     0.646 , 0.0203, 0.    , 0.    , 0.    , 0.    , 0.    , 0.9012,
                     0.1651, 0.167 , 0.1665, 0.1665, 0.2029, 0.0694, 0.    , 0.1683,
                     0.168 , 0.5223, 0.0012, 0.1643, 0.0008, 0.1663, 0.163 , 0.1651,
                     0.    , 0.    , 0.1682, 0.1658, 0.1673, 0.    , 0.    , 0.0999,
                     0.    , 0.3777, 0.0045, 0.1333, 0.964 , 0.    , 0.914 , 0.    ,
                     0.    , 0.4993, 0.1649, 0.7608, 0.    , 0.    , 0.9095, 0.    ,
                     0.1681, 0.1655, 0.    , 0.    , 0.1647, 0.1669, 0.    , 0.    ,
                     0.    , 0.1547, 0.    , 0.    , 0.1676, 0.    , 0.1682, 0.0091,
                     0.1684, 0.    , 0.1563, 0.    , 0.    , 0.0211, 0.0211, 0.    ,
                     0.    , 0.    , 0.0001, 0.157 , 0.    , 0.    , 0.    , 0.    ,
                     0.    , 0.1684, 0.1674, 0.    , 0.    , 0.    , 0.1666, 0.3442])
# fmt: on


def test_morgan_binary(mol, morgan_binary_bits):
    featurizer = MorganBinaryFeaturizer()
    features = featurizer(mol)

    np.testing.assert_array_almost_equal(np.nonzero(features), morgan_binary_bits)


def test_morgan_count(mol, morgan_count_bits, morgan_binary_bits):
    featurizer = MorganCountFeaturizer()
    features = featurizer(mol)

    np.testing.assert_array_almost_equal(features[np.nonzero(features)], morgan_count_bits)


def test_morgan_binary_custom(mol, morgan_binary_custom):
    featurizer = MorganBinaryFeaturizer(radius=3, length=1024)
    features = featurizer(mol)

    np.testing.assert_array_almost_equal(np.nonzero(features), morgan_binary_custom)


def test_rdkit_2d(mol, rdkit_2d_values):
    featurizer = RDKit2DFeaturizer()
    features = featurizer(mol)

    np.testing.assert_array_almost_equal(features, rdkit_2d_values, decimal=2)


def test_v1_rdkit_2d(mol, v1_rdkit_2d_values):
    featurizer = V1RDKit2DFeaturizer()
    features = featurizer(mol)

    np.testing.assert_array_almost_equal(features, v1_rdkit_2d_values, decimal=2)


def test_v1_rdkit_2d_normalized(mol, v1_rdkit_2d_normalized_values):
    featurizer = V1RDKit2DNormalizedFeaturizer()
    features = featurizer(mol)

    np.testing.assert_array_almost_equal(features, v1_rdkit_2d_normalized_values, decimal=2)
