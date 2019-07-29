from tableau.TableauServerConnection import TableauServerConnection
from tableau.config.config import tableau_server_config


def main():
    conn = TableauServerConnection(config_json=tableau_server_config)
    conn.sign_in()
    users = conn.get_users_on_site().json()
    print('Fetched users from server {}'.format(conn.server))
    print(users)
    print(conn.server_info().json())
    conn.sign_out()
