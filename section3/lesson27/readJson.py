import json

with open('arq.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

print(d1_json)
print(d1_json['pessoa1']['nome'])

for k, v in d1_json.items():
    for k1, v1 in v.items():
        print(f'{k1}: {v1}')
    print('-' * 15)