import json
filename = 'data_file.json'
with open(filename) as f_obj:
    data = json.load(f_obj)

print(data)
