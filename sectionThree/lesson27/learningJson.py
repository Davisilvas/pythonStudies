import json

d1 = {
    'pessoa1' : {
        'nome': 'Davi',
        'idade': 21,
        'altura': 1.84,
        'namora': True
    },
    'pessoa2' : {
        'nome': 'Maria',
        'idade': 23,
        'altura': 1.63,
        'namora': True
    }
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('arq.json', 'w+') as arqJson:
    arqJson.write(d1_json)