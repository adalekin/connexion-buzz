import pytest

import connexion_buzz


def test_raise():
    with pytest.raises(connexion_buzz.ConnexionBuzz) as err_info:
        raise connexion_buzz.ConnexionBuzz('i failed')
    assert 'i failed' in str(err_info.value)
