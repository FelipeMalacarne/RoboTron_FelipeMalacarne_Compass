*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /login
Library              RequestsLibrary

*** Variables ***
&{login}=    email=fulano@qa.com    password=teste   
${response} 


*** Keywords ***
POST Endpoint /login
    ${response}                 POST On Session    serverest    /login    json=${login}
    Log To Console              ${response.content}
    Set Global Variable         ${response}

Validar Ter Logado
    Should Be Equal        ${response.json()["message"]}    Login realizado com sucesso
    Should Not Be Empty    ${response.json()["authorization"]} 

Fazer Login e Armazenar Token
    POST Endpoint /login
    Validar Ter Logado
    ${token_auth}        Set Variable    ${response.json()["authorization"]}   
    Log To Console    Token Salvo: ${token_auth}
    Set Global Variable         ${token_auth}     