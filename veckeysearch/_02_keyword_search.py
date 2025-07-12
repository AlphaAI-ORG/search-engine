from .state import State
from .utils import connect_db

def keyword_search(state : State, config):
    user_query = state["user_query"]
    
    index_name = state["index_name"]
    search_num = state["search_num"]
    
    host = config['metadata']['host']
    port = config['metadata']['port']
    auth = (config['metadata']['id'], config['metadata']['pwd'])
    client = connect_db(host,port,auth)

    keyword_hits = client.search(
        index=index_name,
        body={
            "size": search_num,
            "_source": {"excludes": ["chunk_embedding", "chunk_embedding_1024"]}, 
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": user_query,
                            "fields": ["chunk_text", "title"]
                        }
                    },
                    "filter": {
                        "terms": {
                            "title.keyword": state["target_docs"]
                        }
                    }
                }
            }
        }
    )["hits"]["hits"]

    return {"keyword_hits": keyword_hits}
