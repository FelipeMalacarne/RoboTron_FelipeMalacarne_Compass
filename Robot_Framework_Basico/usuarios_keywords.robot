*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /usuarios
Library              RequestsLibrary

*** Variables ***
${URL} =     http://localhost:3000    
${response}
${user_id}  


*** Keywords ***
GET Endpoint /Usuarios
    ${response}                 GET On Session    serverest    /usuarios
    Set Global Variable         ${response} 

POST Endpoint /Usuarios
    &{payload}                 Create Dictionary    nome=felipe.malacarne  password=123    email=felipe.malacarne@gmail.com    administrador=true   
    ${response}                POST On Session    serverest    /usuarios    data=&{payload}
    Set Global Variable        ${user_id}    ${response.json()["_id"]}
    Set Global Variable        ${response} 

PUT Endpoint /usuarios
    &{payload}                  Create Dictionary    nome=cobalto    password=123    email=cobalto60@gmail.com    administrador=true   
    ${response}                 PUT On Session    serverest    /usuarios/${user_id}   data=&{payload}
    Set Global Variable         ${response} 

DELETE Endpoint /usuarios
    ${response}                 DELETE On Session    serverest    /usuarios/${user_id}
    Set Global Variable         ${response} 
