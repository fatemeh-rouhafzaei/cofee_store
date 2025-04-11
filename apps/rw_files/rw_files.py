import json
class RWFiles:
    def __init__(self):
        pass

    def read_json(self, path):
        # Opening JSON file
        with open(path, 'r' , encoding= 'utf-8') as openfile:
            # Reading from json file
            return json.load(openfile)

    def write_json(self, data , path):
        with open(path, "w", encoding= 'utf-8') as outfile:
            json.dump(data, outfile,ensure_ascii=False, indent= 4)
