from typing import TypedDict, Literal
from pydantic import BaseModel, Field # TODO : result basemodel class


class State(TypedDict):

    # input
    search_method : Literal['keyword','vector','hybrid']
    user_query : str

    #config
    search_num : int
    index_name : str
    
    # search results
    keyword_hits : list
    vector_hits : list
    hybrid_hits : list

    # output
    search_results : list