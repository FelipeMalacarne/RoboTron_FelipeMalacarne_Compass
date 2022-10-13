*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /login
Library              RequestsLibrary

*** Variables ***
&{login}=    email=fulano@qa.com    password=teste   


*** Keywords ***
POST Endpoint /login
    ${response}                 POST On Session    serverest    /login    json=${login}
    Log To Console              ${response.content}
    Set Global Variable         ${response}

