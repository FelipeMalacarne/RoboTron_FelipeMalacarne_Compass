import json


#"json.load(string)" transforma uma string em um python dict 
def getJSON(file_path):
    with open(file_path, encoding="UTF-8") as json_origem:
        dict_json = json.load(json_origem)
    return dict_json

user = getJSON("TesteLeituraJSON.json")
print(user["username"])

print(f"Status atual: {user['status']}")
print("Troca de status para off")
user["status"] = "off"
print(f"Status atual: {user['status']}")

print (user["status"])

#"json.dumps(dict)" transforma um dict em um JSON (uma string?)
json_real = json.dumps(user)

