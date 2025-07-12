from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from .state import State
from ._01_preprocessor import preprocessor
from ._02_keyword_search import keyword_search
from ._03_vector_search import vector_search
from ._04_rrf import rrf
from ._05_postprocessor import postprocessor

def start_branch(state : State) :
    search_method = state["search_method"]
    if search_method == 'keyword':
        return 'keyword_search'
    elif search_method == 'vector':
        return 'vector_search' 
    elif search_method == 'hybrid':
        return ['keyword_search','vector_search']  
    else :
        raise ValueError(f'Unknown method: {search_method}')
    
def method_conditions(state : State):
    search_method = state["search_method"]
    if search_method == 'keyword':
        return 'keyword_search'
    elif search_method == 'vector':
        return 'vector_search' 
    elif search_method == 'hybrid':
        return 'hybrid_search'
    else :
        raise ValueError(f'Unknown method: {search_method}')

# Add nodes
builder = StateGraph(State)
builder.add_node("preprocessor", preprocessor)
builder.add_node("keyword_search", keyword_search)
builder.add_node("vector_search", vector_search)
builder.add_node("rrf", rrf)
builder.add_node("postprocessor",postprocessor)

# Add edges
builder.add_edge(START, "preprocessor")
builder.add_conditional_edges(
    "preprocessor",
    start_branch,
)

builder.add_conditional_edges(
    "keyword_search",
    method_conditions,
    {
        "keyword_search" : "postprocessor",
        "hybrid_search": "rrf"
    }
)
builder.add_conditional_edges(
    "vector_search",
    method_conditions,
    {
        "vector_search" : "postprocessor",
        "hybrid_search": "rrf"
    }
)
builder.add_edge("rrf","postprocessor")
builder.add_edge("postprocessor",END)

#memory = MemorySaver()
graph = builder.compile()
