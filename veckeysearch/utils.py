from opensearchpy import OpenSearch

def connect_db(host: str, port: int, auth: tuple) -> OpenSearch:
    
    client = OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=False,
        ssl_show_warn=False,
    )
    return client
