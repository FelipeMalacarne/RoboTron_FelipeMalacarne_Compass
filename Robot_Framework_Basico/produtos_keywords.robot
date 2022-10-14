*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /produtos
Library              RequestsLibrary

*** Variables ***

*** Keywords ***
GET Endpoint /produtos
    ${response}                 GET On Session    serverest    /produtos
    Status Should Be    200

GET Endpoint /produtos/"${_id}" 
    ${response}                 GET On Session    serverest    /produtos/${_id}
    Set Global Variable         ${response} 
POST Endpoint /produtos
    &{post_body}     Create Dictionary    nome=LogitREWREEEEECH    preco=47   descricao=MousEEEE     quantidade=3821
    ${header}        Create Dictionary    Authorization=${token_auth}    
    ${response}      POST On Session    serverest    /produtos    data=${post_body}  headers=${header}  expected_status=anything
    Log To Console    ${response.content}
    Set Global Variable    ${response}

 DELETE Endpoint /produtos
    ${header}        Create Dictionary    Authorization=${token_auth}    
    ${response}      DELETE On Session    serverest    /produtos/${id_produto}    headers=${header}  expected_status=anything
    Log To Console    ${response.content}
    Set Global Variable    ${response}

Validar Ter Criado Produto
    Should Be Equal        ${response.json()["message"]}    Cadastro realizado com sucesso
    Should Not Be Empty    ${response.json()["_id"]} 

Criar Produto e Armazenar ID
    POST Endpoint /produtos
    Validar Ter Criado Produto
    ${id_produto}        Set Variable    ${response.json()["_id"]}   
    Log To Console    ${id_produto}
    Set Global Variable    ${id_produto}