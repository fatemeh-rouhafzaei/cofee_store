import json
class RWFiles:
    def __init__(self , file_name):
        self.file_name = file_name

    def read_json(self):
        # Opening JSON file
        with open(self.file_name, 'r' , encoding= 'utf-8') as openfile:
            # Reading from json file
            return json.load(openfile)

    def write_json(self, data):
        with open(self.file_name, "w", encoding= 'utf-8') as outfile:
            json.dump(data, outfile,ensure_ascii=False, indent= 4)
