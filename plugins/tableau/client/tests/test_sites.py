from tableau.client.TableauServerConnection import TableauServerConnection
from tableau.client.config.config import tableau_server_config

TEST_SITE_NAME = 'estam_api_test'
TEST_SITE_CONTENT_URL = 'estam_api_test'
UPDATED_CONTENT_URL = 'estam_api_test_renamed'


def sign_in():
    conn = TableauServerConnection(tableau_server_config)
    conn.sign_in()
    return conn


def sign_out(conn):
    conn.sign_out()


def create_site(conn, site_name, site_content_url):
    response = conn.create_site(site_name, site_content_url)
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


def test_create_site():
    conn = sign_in()
    conn, create_site_response = create_site(conn, TEST_SITE_NAME, TEST_SITE_NAME)
    assert create_site_response.status_code == 201
    conn.sign_out()


def test_query_site():
    conn = sign_in()
    conn, query_site_response = query_site(conn)
    assert query_site_response.status_code == 200
    conn.sign_out()


def test_query_sites():
    conn = sign_in()
    conn, query_sites_response = query_sites(conn)
    assert query_sites_response.status_code == 200
    conn.sign_out()


def test_query_views_for_site():
    conn = sign_in()
    conn, query_views_for_site_response = query_views_for_site(conn)
    assert query_views_for_site_response.status_code == 200
    conn.sign_out()


def test_update_site():
    conn = sign_in()
    conn.switch_site(TEST_SITE_CONTENT_URL)
    conn, update_site_response = update_site_name(conn, UPDATED_CONTENT_URL)
    assert update_site_response.status_code == 200
    conn.sign_out()


def test_delete_site():
    conn = sign_in()
    conn.switch_site(UPDATED_CONTENT_URL)
    conn, delete_site_response = delete_site(conn)
    assert delete_site_response.status_code == 204
    conn.sign_out()
