*** Settings ***
Documentation     Arquvo simples para realizar requsisões HTTP em APIs
Library           RequestsLibrary

*** Variables ***
&{login}=    email=fulano@qa.com    password=teste       
${response}
&{post_body}

*** Test Cases ***
Cenario: GET Todos os Usuarios 200
    Criar Sessao
    Realizar Login
    GET Endpoint /Usuarios
    Validar Status Code "200"

Cenario: GET Todos produtos
    Criar Sessao
    Realizar Login
    GET Endpoint /produtos

Cenario: GET produto por Id
    Criar Sessao
    Realizar Login
    GET Endpoint /produtos/"BeeJh5lz3k6kSIzA"
   
   
*** Keywords ***
Criar Sessao          
    Create Session         serverest    https://serverest.dev
GET Endpoint /Usuarios
    ${response}            GET On Session    serverest    /usuarios
    Set Global Variable    ${response} 

GET Endpoint /produtos
    ${response}            GET On Session    serverest    /produtos
    Status Should Be    200

GET Endpoint /produtos/"${_id}"
    ${response}            GET On Session    serverest    /produtos/${_id}
    Set Global Variable    ${response} 

Validar Status Code "${statuscode}"
    Should Be True    ${response.status_code} == ${statuscode}




# POST Endpoint /produtos
#     &{post_body}=    Create Dictionary    nome=Logitech MX Vertical    preco=470    descricao=Mouse     quantidade=381    _id=BeeJh5lz3k6kSIzA

#     ${response}    POST On Session    serverest    /produtos    json=${post_body}    expected_status=anything
#     Set Global Variable    &{post_body}
#     Set Global Variable    ${response}


Realizar Login
    ${response}    POST On Session    serverest    /login    json=${login}
    Status Should Be    200
    
