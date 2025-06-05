from opensearchpy import OpenSearch

def connect_db():

    host = "localhost"
    port = 9200
    auth = ("admin", "Kimjung5309!")

    client = OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=False,
        ssl_show_warn=False,
    )
    return client 