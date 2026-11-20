import json
import requests

baseUri = "http://localhost:58000/api/v1"

# Obtener ticket
headers = {"Content-Type": "application/json"}
data = json.dumps({"username": "cisco", "password": "cisco123!"})
resp = requests.post(baseUri + "/ticket", data=data, headers=headers)
ticket = resp.json()["response"]["serviceTicket"]

# Consultar hosts
headers = {"X-Auth-Token": ticket}
resp = requests.get(baseUri + "/host", headers=headers)
hosts = resp.json()["response"]

buscar = input("Ingresá IP o nombre del host a buscar: ")

for host in hosts:
    if buscar in host["hostName"] or buscar in host["hostIp"]:
        print("Host:", host["hostName"], "| IP:", host["hostIp"], "| Puerto:", host["connectedInterfaceName"])