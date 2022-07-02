import requests
url = "http://httpbin.org/post"

datos = {
    'lenguaje': 'Pyhton',
    'version' : '3.7.3'
}

headers = {
    'User-agent' : 'PythonAgent',
    'Agent-Version' : '1.0.0'
}

r = requests.post(url, data=datos, headers=headers)

respuesta = r.text
print(respuesta)