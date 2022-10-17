*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /login
Library              RequestsLibrary
Resource             common.robot

*** Variables ***
&{login}=    email=fulano@qa.com    password=teste   
${response} 


*** Keywords ***
POST Endpoint /login
    ${response}                 POST On Session    serverest    /login    json=${payload}    expected_status=anything 
    Set Global Variable         ${response}

Validar Ter Logado
    Should Be Equal        ${response.json()["message"]}    Login realizado com sucesso
    Should Not Be Empty    ${response.json()["authorization"]} 
    Status Should Be    200

Fazer Login e Armazenar Token
    POST Endpoint /login
    Validar Ter Logado
    ${token_auth}        Set Variable    ${response.json()["authorization"]}   
    Log To Console    Token Salvo: ${token_auth}
    Set Global Variable         ${token_auth}     

POST Login User Invalido 401
    ${json}        Importar Json Estatico    login.json
    ${payload}    Set Variable    ${json["user_invalido"]}
    Set Global Variable    ${payload}
    POST Endpoint /login
    Status Should Be    401

POST Login User Sem Senha 400
    ${json}        Importar Json Estatico    login.json
    ${payload}    Set Variable    ${json["user_sem_senha"]}
    Set Global Variable    ${payload}
    POST Endpoint /login
    Status Should Be    400

POST Login User Sem Email 400
    ${json}        Importar Json Estatico    login.json
    ${payload}    Set Variable    ${json["user_sem_email"]}
    Set Global Variable    ${payload}
    POST Endpoint /login
    Status Should Be    400

POST Login Usuario Valido 200
    ${json}        Importar Json Estatico    login.json
    ${payload}    Set Variable    ${json["user_valido"]}
    Set Global Variable    ${payload}
    POST Endpoint /login
    Status Should Be    200


    
