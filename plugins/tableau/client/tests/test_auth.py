from tableau.client.TableauServerConnection import TableauServerConnection
from tableau.client.config.config import tableau_server_config


def get_auth_responses():
    conn = TableauServerConnection(tableau_server_config)
    sign_in_response = conn.sign_in()
    sign_out_response = conn.sign_out()
    return sign_in_response, sign_out_response


def test_auth():
    sign_in_response, sign_out_response = get_auth_responses()
    assert sign_in_response.status_code == 200
    assert sign_out_response.status_code == 204


test_auth()
