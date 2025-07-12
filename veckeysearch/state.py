from typing import TypedDict, Literal, List

class State(TypedDict):

    # input
    search_method : Literal['keyword','vector','hybrid']
    user_query : str
    search_num : int
    target_docs : List[str]
    #config
    index_name : str
    
    # search results
    keyword_hits : list
    vector_hits : list
    hybrid_hits : list

    # output
    search_results : list