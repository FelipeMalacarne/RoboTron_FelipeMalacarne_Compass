*** Settings ***
Documentation     Arquvo simples para realizar requsisões HTTP em APIs
Library           RequestsLibrary

*** Variables ***
${URL} =     http://localhost:3000
&{login}=    email=fulano@qa.com    password=teste       
${response}


*** Test Cases ***

##Aula dia 4
Cenario: GET Todos os Usuarios 200
    [Tags]    GET
    Criar Sessao
    Realizar Login
    GET Endpoint /Usuarios
    Validar Status Code "200"
    Validar Quantidade "${4}"
    Printar Response

Cenario: GET Todos produtos 200
    [Tags]    GET
    Criar Sessao
    Realizar Login
    GET Endpoint /produtos

Cenario: GET produto por Id 200
    [Tags]    GET
    Criar Sessao
    Realizar Login
    GET Endpoint /produtos/"BeeJh5lz3k6kSIzA"
    Validar Status Code "200"

##Aula dia 5
Cenario: POST Cadastrar Usuario 201
    [Tags]    POST
    Criar Sessao
    POST Endpoint /Usuarios
    Validar Status Code "201"
    Validar Se Mensagem Contem "sucesso"

Cenario: PUT Editar Usuario 200
    [Tags]    PUT
    Criar Sessao
    PUT Endpoint /Usuarios
    Validar Status Code "200"
    
Cenario: DELETE Usuario 200
    [Tags]    DELETE
    Criar Sessao
    DELETE Endpoint /usuarios
    Validar Status Code "200"



*** Keywords ***
Criar Sessao          
    Create Session              serverest    ${URL}
GET Endpoint /Usuarios
    ${response}                 GET On Session    serverest    /usuarios
    Set Global Variable         ${response} 

GET Endpoint /produtos
    ${response}                 GET On Session    serverest    /produtos
    Status Should Be    200

GET Endpoint /produtos/"${_id}"
    ${response}                 GET On Session    serverest    /produtos/${_id}
    Set Global Variable         ${response} 

Validar Status Code "${statuscode}"
    Should Be True             ${response.status_code} == ${statuscode}

POST Endpoint /Usuarios
    &{payload}                 Create Dictionary    nome=felipe.malacarne12   password=123    email=feleepe12.m@gmail.com    administrador=true   
    ${response}                POST On Session    serverest    /usuarios    data=&{payload}
    Log To Console             Response:${response.content}
    Set Global Variable        ${response} 


# POST Endpoint /produtos
#     &{post_body}=    Create Dictionary    nome=Logitech MX Vertical    preco=470    descricao=Mouse     quantidade=381    _id=BeeJh5lz3k6kSIzA

#     ${response}    POST On Session    serverest    /produtos    json=${post_body}    expected_status=anything
#     Set Global Variable    &{post_body}
#     Set Global Variable    ${response}

PUT Endpoint /usuarios
    &{payload}                  Create Dictionary    nome=saaas    password=123    email=felllipe.m@gmail.com    administrador=true   
    ${response}                 PUT On Session    serverest    /usuarios/qF56BeDh6AfIq4WW    data=&{payload}
    Log To Console              ${response.content}
    Set Global Variable         ${response} 

DELETE Endpoint /usuarios
    ${response}                 DELETE On Session    serverest    /usuarios/qF56BeDh6AfIq4WW
    Log To Console              ${response.content}
    Set Global Variable         ${response} 

Realizar Login
    ${response}                 POST On Session    serverest    /login    json=${login}
    Status Should Be            200

Validar Quantidade "${qnt}"
    Should Be Equal    ${response.json()["quantidade"]}    ${qnt}

Validar Se Mensagem Contem "${palavra}"
    Should Contain    ${response.json()["message"]}    ${palavra}

Printar Response
    Log to Console    ${response.json()["usuarios"][2]["nome"]}