import json
from datetime import datetime


def save_interaction(file_path,query,response) :
   
    record = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "response": response,
    }

    with open(file_path, "a") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")
        