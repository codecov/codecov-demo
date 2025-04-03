from api.smiles.smiles import Smiles


def test_smile():
    assert Smiles().smile() == ":)"
