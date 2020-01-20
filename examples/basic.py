import http

import connexion

import connexion_buzz


class MyException(connexion_buzz.ConnexionBuzz):
    status_code = http.HTTPStatus.BAD_REQUEST


def index():
    raise MyException("basic test")


app = connexion.FlaskApp(__name__, specification_dir="openapi/")
app.app.register_error_handler(
    connexion_buzz.ConnexionBuzz, connexion_buzz.ConnexionBuzz.build_error_handler(),
)

app.add_api("my_api.yaml")
app.run(port=8080)
