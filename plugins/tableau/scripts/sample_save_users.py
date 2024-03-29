import os
import pandas as pd

from tableau_api_lib import TableauServerConnection
from tableau.config.config import tableau_server_config


def main():
    print(pd.datetime.now())
    conn = TableauServerConnection(config_json=tableau_server_config)
    conn.sign_in()
    print(os.listdir(os.getcwd()))
    users_json = conn.get_users_on_site().json()
    print(users_json)
    conn.sign_out()


if __name__ == '__main__':
    main()
