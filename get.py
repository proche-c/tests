import requests 
import io
import json

url = "https://api.github.com/events"

r = requests.get(url)

print (r.status_code)
print (r.reason)
print("*****************")
print(type(r.text))
#print(dir(r.text))
#print(dir(r))
print("*****************")
#print(r.request)
#print("*****************CABEZERA PETICION")
#print(dir(r.request.headers))
print(r.request.headers)
#print("*****************CABEZERA RESPUESTA")
#print(r.headers)
#print("*****************")
#print(r.request.url)
#print("*****************")
#print(r.cookies)
#print("*****************")
#print(r.ok)
#print("***obtener cuerpo en json**")
data = r.json()
print(type(data))
print("***********")
print(dir(data))
#print(data)
#print("***IMPRIMIENDO DATA***")
#print(data['results'])
#print(dir(r.json))
#print(r.text)
#print (r.__sizeof__)
#print(r.content)
#data = r.json()
#print("*****************")
#print(data)
#****ESCRIBIMOS LA RESPUESTA EN UN FICHERO JSON***
with open("respuesta.html", "w", encoding="utf-8") as f:
    f.write(r.text)
#se crea f y lo podemos abrir
#hacer creer al navegador que estamos realizando 
# la peticion a traves de la web, tenemos que personalizar
#  el user-agent del request.header
h = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
#para saber el user-agent del chrome que tenemos instalado ir a
#web whatismybrowser.com
r = requests.get(url, headers=h)
print(r.request.headers)