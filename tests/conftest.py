import connexion

import pathlib

import pytest

import connexion_buzz

TEST_FOLDER = pathlib.Path(__file__).parent
FIXTURES_FOLDER = TEST_FOLDER / 'fixtures'
SPEC_FOLDER = TEST_FOLDER / 'fakeapi'


@pytest.fixture(scope='session')
def app():
    application = connexion.FlaskApp(__name__, specification_dir=FIXTURES_FOLDER, debug=True)
    application.add_api('hello_api.yaml')

    application.app.register_error_handler(
        connexion_buzz.ConnexionBuzz,
        connexion_buzz.ConnexionBuzz.build_error_handler(
            lambda e: print('description: ', e.description),
            lambda e: print('status_code: ', e.status_code),
        ),
    )

    with application.app.app_context():
        yield application.app
