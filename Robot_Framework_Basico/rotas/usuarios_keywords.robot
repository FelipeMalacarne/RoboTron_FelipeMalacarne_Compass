*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /usuarios
Library              RequestsLibrary
Resource             common.robot

*** Variables ***
${URL} =     http://localhost:3000    
${response}
${user_id}  


*** Keywords ***
GET Endpoint /Usuarios
    ${response}                 GET On Session    serverest    /usuarios
    Set Global Variable         ${response} 


Validar GET Usuarios
    Status Should Be        200
    Should Not Be Empty     ${response.json()["usuarios"]}
POST Endpoint /Usuarios
    ${response}                POST On Session    serverest    /usuarios    json=&{payload}
    Set Global Variable        ${user_id}    ${response.json()["_id"]}
    Set Global Variable        ${response} 

PUT Endpoint /usuarios
    &{payload}                  Create Dictionary    nome=cobalto    password=123    email=cobalto60@gmail.com    administrador=true   
    ${response}                 PUT On Session    serverest    /usuarios/${user_id}   json=&{payload}
    Set Global Variable         ${response} 

DELETE Endpoint /usuarios
    ${response}                 DELETE On Session    serverest    /usuarios/${user_id}
    Set Global Variable         ${response} 

Criar Usuario Estatico Valido
    ${json}        Importar Json Estatico    usuarios.json
    ${payload}    Set Variable    ${json["user_valido"]}
    Set Global Variable    ${payload}
