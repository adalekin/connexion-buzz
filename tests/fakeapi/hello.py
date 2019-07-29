import http

import connexion_buzz


class OverloadBuzz(connexion_buzz.ConnexionBuzz):
    status_code = http.HTTPStatus.UNAUTHORIZED


def index():
    raise connexion_buzz.ConnexionBuzz('basic test')


def status():
    raise OverloadBuzz('status test')
