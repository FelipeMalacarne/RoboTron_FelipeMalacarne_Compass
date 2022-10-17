*** Settings ***
Documentation     Arquvo simples para realizar requsisões HTTP em APIs
Library           RequestsLibrary
Resource          ./rotas/usuarios_keywords.robot
Resource          ./rotas/produtos_keywords.robot
Resource          ./rotas/login_keywords.robot
Resource          ./rotas/carrinho.keywords.robot
Resource          ./rotas/common.robot
*** Variables ***
${URL} =     http://localhost:3000
&{login}=    email=fulano@qa.com    password=teste       
${response}
${user_id}  


*** Test Cases ***

Cenario: Geral Rota Login
    [Tags]    ROTAS
    Criar Sessao
    POST Login User Invalido 401                     ## A documentação não menciona o status code 401
    POST Login User Sem Senha 400
    POST Login User Sem Email 400
    POST Login Usuario Valido 200
    Validar Ter Logado

Cenario: Geral Rota Usuarios
    [Tags]    ROTAS
    Criar Sessao
    GET Endpoint /Usuarios
    POST Usuarios User Cadastrado 400 
    POST Usuarios User Sem Email 400
    POST Usuarios User Sem Senha 400
    POST Usuarios User Valido 201                     #Deve retornar 201 e criar usuário com sucesso
    GET Usuario por ID 200                            #Deve retornar o json do usuario criado
    DELETE Endpoint /usuarios Ultimo ID               #Deletar usuario Criado
    GET Usuario por ID 400                            #Deve retornar 400 pois o usuario foi deletado


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
    DELETE Endpoint /usuarios Ultimo ID
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
    Should Contain             ${response.json()["message"]}    ${palavra}

    

