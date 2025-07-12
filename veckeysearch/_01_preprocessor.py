from .state import State

def preprocessor(state : State, config):
    
    index_name = config['metadata']['index_name']
    
    return {"index_name":index_name}