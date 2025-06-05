from .state import State

def postprocessor(state : State):

    search_method = state["search_method"]
    if search_method == "keyword" :
        hits = "keyword_hits"
    elif search_method == "vector" :
        hits = "vector_hits"
    else :
        hits = "hybrid_hits"

    search_results = state[hits]
    
    return {"search_results": search_results}