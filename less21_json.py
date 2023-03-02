

import json

auto1 = {
    'vendor': 'vw',
    'model': 'polo',
    'hp': 90,
    'komplekt': ['gur', 'kondey', 'radio']
    }

auto2 = {
    'vendor': 'азлк',
    'model': 'москвич 3',
    'hp': 153,
    'komplekt': ['seatheat', 'climate', 'mp3cd']
    }

dasautos = []

dasautos.append(auto1)
dasautos.append(auto2)

json_data = json.dumps(dasautos)
print(json_data)
# // save JSON ================================================================
filename = 'less21_json.json'
file1 = open(filename, 'w')
json.dump(dasautos, file1)
file1.close()
# // load JSON ================================================================
file2 = open(filename, 'r')
json_from = []
json_from = json.load(file2)
file2.close()
print("===========================================================")
print(json_from)

for ind, auto3 in enumerate(json_from, 1):
    print("В НАЛИЧИИ: ", ind, str(auto3['vendor']).upper(), str(auto3['model']).title(),
    auto3['hp'], "л.с., КОМПЛЕКТАЦИЯ: ", auto3['komplekt'])