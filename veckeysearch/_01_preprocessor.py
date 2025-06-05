from .state import State

def preprocessor(state : State, config):
    
    index_name = config['metadata']['index_name']
    search_num = config['metadata']['search_num']
    
    return {"search_num":search_num, "index_name":index_name}