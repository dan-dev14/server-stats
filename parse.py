import pickle
from pprint import pprint as pp

data = []
with open("save.p", "rb") as f:
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break
pp(data)