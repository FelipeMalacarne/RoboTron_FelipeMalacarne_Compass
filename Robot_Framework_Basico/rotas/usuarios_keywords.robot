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
    Status Should Be        200
    Should Not Be Empty     ${response.json()["usuarios"]}


POST Endpoint /Usuarios
    ${response}                POST On Session    serverest    /usuarios    json=&{payload}    expected_status=anything
    # Set Global Variable        ${user_id}    ${response.json()["_id"]}
    Set Global Variable        ${response} 

PUT Endpoint /usuarios
    &{payload}                  Create Dictionary    nome=cobalto    password=123    email=cobalto60@gmail.com    administrador=true   
    ${response}                 PUT On Session    serverest    /usuarios/${user_id}   json=&{payload}
    Set Global Variable         ${response} 

DELETE Endpoint /usuarios Ultimo ID
    ${response}                 DELETE On Session    serverest    /usuarios/${user_id}
    Set Global Variable         ${response} 

Criar Usuario Estatico Valido
    ${json}        Importar Json Estatico    usuarios.json
    ${payload}    Set Variable    ${json["user_valido"]}
    Set Global Variable    ${payload}

 POST Usuarios User Cadastrado 400 
    Criar Payload Estatico "usuarios.json" "user_invalido"
    POST Endpoint /Usuarios
    Status Should Be    400
    Should Be Equal        ${response.json()["message"]}    Este email já está sendo usado

POST Usuarios User Sem Email 400
    Criar Payload Estatico "usuarios.json" "user_sem_email"
    POST Endpoint /Usuarios
    Status Should Be    400

POST Usuarios User Sem Senha 400
    Criar Payload Estatico "usuarios.json" "user_sem_senha"
    POST Endpoint /Usuarios
    Status Should Be    400

POST Usuarios User Valido 201
    Criar Payload Estatico "usuarios.json" "user_valido"
    POST Endpoint /Usuarios
    Should Be Equal        ${response.json()["message"]}    Cadastro realizado com sucesso
    Should Not Be Empty    ${response.json()["_id"]}
    Set Global Variable        ${user_id}    ${response.json()["_id"]}
    Status Should Be    201

GET Usuario por ID 200
    ${response}                 GET On Session    serverest    /usuarios/${user_id}
    Should Not Be Empty    ${response.json()["nome"]}
    Status Should Be    200

GET Usuario por ID 400
    ${response}                 GET On Session    serverest    /usuarios/${user_id}    expected_status=anything
    Should Be Equal        ${response.json()["message"]}    Usuário não encontrado
    Status Should Be    400   