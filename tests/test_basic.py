import json

import connexion_buzz

from . import utils


def test_basic_functionality(app, capsys):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == connexion_buzz.ConnexionBuzz.status_code
    response_json = json.loads(response.get_data(as_text=True))
    assert response_json['description'] == 'basic test'

    (out, err) = capsys.readouterr()
    assert utils.stripped('description: basic test') in utils.stripped(out)


def test_basic_overloaded_status_code(app):
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 401
    response_json = json.loads(response.get_data(as_text=True))
    assert response_json['description'] == 'status test'
