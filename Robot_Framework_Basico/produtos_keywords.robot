*** Settings ***
Documentation        Keywords e Variaveis para o endpoint /produtos
Library              RequestsLibrary

*** Variables ***
${token_auth}     Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZ1bGFub0BxYS5jb20iLCJwYXNzd29yZCI6InRlc3RlIiwiaWF0IjoxNjY1NjY4MTQyLCJleHAiOjE2NjU2Njg3NDJ9.2_VTdNWH5NqpjAIz7ZqZ7k2Zf6N_8tPRH5weKeua-PM


*** Keywords ***
GET Endpoint /produtos
    ${response}                 GET On Session    serverest    /produtos
    Status Should Be    200

GET Endpoint /produtos/"${_id}" 
    ${response}                 GET On Session    serverest    /produtos/${_id}
    Set Global Variable         ${response} 
POST Endpoint /produtos
    &{post_body}     Create Dictionary    nome=Logit    preco=47   descricao=MousE     quantidade=3821
    ${header}        Create Dictionary    Authorization=${token_auth}    
    ${response}      POST On Session    serverest    /produtos    data=${post_body}  headers=${header}  expected_status=anything
    Log To Console    ${response.content}
    Set Global Variable    ${response}
