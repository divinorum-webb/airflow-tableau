from tableau.client.TableauServerConnection import TableauServerConnection
from tableau.client.config.config import tableau_server_config


def sign_in():
    conn = TableauServerConnection(tableau_server_config)
    conn.sign_in()
    return conn


def sign_out(conn):
    conn.sign_out()


def create_site(conn, site_name, site_content_url):
    response = conn.create_site(site_name, site_content_url)
    return conn, response


def switch_site(conn, new_site_name):
    response = conn.switch_site(new_site_name)
    return conn, response


def query_site(conn):
    response = conn.query_site()
    return conn, response


def query_sites(conn):
    response = conn.query_sites()
    return conn, response


def query_views_for_site(conn):
    response = conn.query_views_for_site()
    return conn, response


def update_site_name(conn, new_content_url):
    site_json = conn.query_site().json()
    site_id = site_json['site']['id']
    response = conn.update_site(site_id=site_id, content_url=new_content_url)
    return conn, response


def delete_site(conn):
    site_json = conn.query_site().json()
    site_id = site_json['site']['id']
    response = conn.delete_site(site_id=site_id)
    return conn, response


def test_site_methods():
    conn = sign_in()

    conn, create_site_response = create_site(conn, 'estam_api_test', 'estam_api_test')
    assert create_site_response.status_code == 201

    conn, switch_site_response = switch_site(conn, 'estam_api_test')
    assert switch_site_response.status_code == 200

    conn, query_site_response = query_site(conn)
    assert query_site_response.status_code == 200

    conn, query_sites_response = query_sites(conn)
    assert query_sites_response.status_code == 200

    conn, query_views_for_site_response = query_views_for_site(conn)
    assert query_views_for_site_response.status_code == 200

    conn, update_site_response = update_site_name(conn, 'estam_api_test_renamed')
    assert update_site_response.status_code == 200

    conn, delete_site_response = delete_site(conn)
    assert delete_site_response.status_code == 204

    sign_out(conn)


test_site_methods()
