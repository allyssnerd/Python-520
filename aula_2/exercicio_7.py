
import numpy as np

A = np.array([
    [ 2, 2 ],
    [ 3, 3 ]
])

B = np.array([
    [ 2, 2 ],
    [ 3, 3 ]
])

print(A * B)

exit()

import json

import requests


cep = input('Digite seu cep: ')

URL = 'https://viacep.com.br/ws/{}/json/unicode/'.format(cep)
res = requests.get(URL)

print(json.dumps(res.json(), indent=2))

