from .state import State
from .utils import connect_db

def keyword_search(state : State):
    user_query = state["user_query"]
    
    index_name = state["index_name"]
    search_num = state["search_num"]
    client = connect_db()

    keyword_hits = client.search(
            index=index_name,
            body={
                    "size":search_num,
                    "_source": {"excludes": ["chunk_embedding","chunk_embedding_1024"]}, 
                    "query":{
                        "multi_match":{
                            "query": user_query,
                            "fields" : ["chunk_text"]

                        }
                    }
                }
            )["hits"]["hits"]

    return {"keyword_hits": keyword_hits}
