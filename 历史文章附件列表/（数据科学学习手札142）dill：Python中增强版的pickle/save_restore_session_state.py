import dill
from pprint import pprint

dill.load_session('./session_state.pkl')

pprint(restore_demo)