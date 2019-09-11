import pandas as pd

from tableau_api_lib import TableauServerConnection
from tableau.config.config import tableau_server_config


def main():
    conn = TableauServerConnection(config_json=tableau_server_config)
    conn.sign_in()
    users = conn.get_users_on_site().json()
    print("pandas datetime: ", pd.datetime.now())
    print('Fetched users from server {}'.format(conn.server))
    print(users)
    print(conn.server_info().json())
    conn.sign_out()


def query_user(**kwargs):
    user_id = kwargs['user_id']
    conn = TableauServerConnection(config_json=tableau_server_config)
    conn.sign_in()
    user_data = conn.query_user_on_site(user_id)
    print(user_data.json())
    conn.sign_out()


if __name__ == '__main__':
    main()
