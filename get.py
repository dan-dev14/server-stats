import os
from subprocess import check_output as co
from pprint import pprint as pp
import pickle
from datetime import datetime

def storage():
    output = run("df -h")
    del output[0]
    return {line.split()[5]: line.split()[4] for line in output}

def run(cmd):
    return co(cmd, shell=True).decode("UTF-8").splitlines()

def log_size():
    size = os.path.getsize("save.p")
    kb = size / 1000
    if kb > 2:
        refresh()
    return kb

def refresh():
    print("Rolling log file")
    os.replace("save.p", "save.bak")

def save(data):
    pickle.dump( data, open( "save.p", "ab" ) )

def timestamp():
    return datetime.now()

if __name__ == '__main__':
    size = log_size()
    print(f"Log is currently {size} KB")
    data = {}
    data["time"] = timestamp()
    data["df"] = storage()
    pp(data)
    save(data)