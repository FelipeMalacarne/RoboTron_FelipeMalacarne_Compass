*** Settings ***
Documentation     Arquvo simples para realizar requsisões HTTP em APIs
Library           RequestsLibrary
Resource          usuarios_keywords.robot
Resource          produtos_keywords.robot
Resource          login_keywords.robot
Resource          common.robot
*** Variables ***
${URL} =     http://localhost:3000
&{login}=    email=fulano@qa.com    password=teste       
${response}
${user_id}  


*** Test Cases ***

##Aula dia 4
Cenario: GET Todos os Usuarios 200
    [Tags]    GET
    Criar Sessao
    GET Endpoint /Usuarios
    Validar Status Code "200"

Cenario: GET Todos produtos 200
    [Tags]    GET
    Criar Sessao
    GET Endpoint /produtos

Cenario: GET produto por Id 200
    [Tags]    GET
    Criar Sessao
    GET Endpoint /produtos/"BeeJh5lz3k6kSIzA"
    Validar Status Code "200"

Cenario: POST Cadastrar Usuario 201
    [Tags]    POST
    Criar Sessao
    POST Endpoint /Usuarios
    Validar Status Code "201"
    Validar Se Mensagem Contem "sucesso"

Cenario: PUT Editar Usuario Criado 200
    [Tags]    PUT
    Criar Sessao
    PUT Endpoint /Usuarios
    Validar Status Code "200"
    
Cenario: DELETE Usuario Editado 200
    [Tags]    DELETE
    Criar Sessao
    DELETE Endpoint /usuarios
    Validar Status Code "200"

Cenario: POST Realizar Login 200
    [tags]    POSTLOGIN
    Criar Sessao
    POST Endpoint /login
    Validar Status Code "200"

Cenario: POST Criar Produto 201
    [Tags]    POSTPRODUTO
    Criar Sessao
    Fazer Login e Armazenar Token
    POST Endpoint /produtos
    Validar Status Code "201"

Cenario: DELETE Excluir Produto 200
    [Tags]    DELETEPRODUTO
    Criar Sessao
    Fazer Login e Armazenar Token
    Criar Produto e Armazenar ID
    DELETE Endpoint /produtos
    Validar Status Code "200"

Cenario: POST Criar Usuario De Massa Estatica 201
    [Tags]    POSTUSUARIOESTATICO
    Criar Sessao
    Criar Usuario Estatico Valido
    POST Endpoint /Usuarios
    Validar Status Code "201"

*** Keywords ***
Criar Sessao          
    Create Session              serverest    ${URL}
Validar Quantidade "${qnt}"
    Should Be Equal            ${response.json()["quantidade"]}    ${qnt}
Validar Se Mensagem Contem "${palavra}"
    Should Contain    ${response.json()["message"]}    ${palavra}

    

