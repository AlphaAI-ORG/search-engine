from .state import State
from .utils import connect_db
from langchain_openai import OpenAIEmbeddings

def _get_embedding(text : str, api_key: str) -> list[float]:

    embeddings_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=api_key,
        )
    
    embedding = embeddings_model.embed_query(text)

    return embedding 

def vector_search(state : State, config):
    user_query = state["user_query"]
    index_name = state["index_name"]
    search_num = state["search_num"]

    client = connect_db()

    api_key = config['metadata']['api_key']
    user_query_vector = _get_embedding(text = user_query, api_key = api_key)

    vector_hits = client.search(
            index=index_name,
            body={
                    "size":search_num,
                    "_source": {"excludes": ["chunk_embedding","chunk_embedding_1024"]}, 
                    "query":{
                        "knn":{
                            "chunk_embedding":{
                                "vector" :user_query_vector,
                                "k": search_num  #? size 랑 모슨 차이?
                            }
                        }
                    }
                }
            )["hits"]["hits"]

    return {"vector_hits": vector_hits}
