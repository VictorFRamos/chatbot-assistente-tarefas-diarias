import json
import os

FILE_NAME = "memory.json"

def load_memory():
    if not os.path.exists(FILE_NAME):
        return {"tasks": []}
    
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=2)

def add_task(task):
    data = load_memory()
    data["tasks"].append(task)
    save_memory(data)

def list_tasks():
    data = load_memory()
    return data["tasks"]
