import json
import os

from tableau.client.tableau_server_connection import TableauServerConnection
from tableau.client.config.config import tableau_server_config


def main():
    conn = TableauServerConnection(config_json=tableau_server_config)
    conn.sign_in()
    print(os.listdir(os.getcwd()))
    users_json = conn.get_users_on_site().json()
    print(users_json)
    conn.sign_out()


if __name__ == '__main__':
    main()
