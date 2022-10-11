# RoboTron_FelipeMalacarne_Compass
Esse repositório é destinado ao cumprimento das tarefas da Sprint 5 do Projeto de Bolsas da Compasso.uol. Essa sprint aborda as funcionalidades básicas do [Robot Framework](http://robotframework.org), Abordagem Keyword-Driven, Automações em APIs, Requests e responses, Autenticação em APIs e manipulação de dados estáticos.

Seu conteudo é a representação de todos conceitos estudados e trabalhados durante esse período.


## ⚙️Tecnologias utilizadas e instalação:
- Python 3.10.7: Você pode fazer o download e instalar a partir do [site oficial do python](https://www.python.org/downloads/)

- Robot Framework: Com o python instalado e o [pip](https://pip.pypa.io/en/stable/) instalado digite o seguinte comando no seu terminal:
```
pip install robotframework
```
- Libraries utilizadas:
    - [Browser Library](https://github.com/MarketSquare/robotframework-browser)

    - [Robotframework-faker](https://github.com/guykisel/robotframework-faker)

    - [HTTPRequests Library](https://github.com/MarketSquare/robotframework-requests#readme)
        ```
        pip install robotframework-browser
        pip install robotframework-faker
        pip install robotframework-requests
        ```
---

## 🔬 Exemplo
Segue abaixo um exemplo simples de um caso de teste para a validação de um login em um determinado sistema. Você consegue achar mais exemplos relacionados com projetos de demonstração em: http://robotframework.org.
```RobotFramework
Documentation     Um suíte de teste com um único teste para um login valido.
...
...               Esse teste tem um fluxo criado usando keywords importadas de um arquivo .resource
...
Resource          login.resource

*** Test Cases ***
Login Valido
    Abrir Browser na Pagina de Login
    Input Username    demo
    Input Password    mode
    Enviar Credenciais
    Welcome Page Deve estar aberta
    [Teardown]    Fechar Browser
```

---

## 🛠️ Uso

Testes e tarefas são executadas pelo terminal, utilizando o comando `robot` ou executando o módulo do robot diretamente : `python -m robot`
Voce pode definir um diretório para enviar os outputs(logs e reports) dos testes.
```
robot -d ./myDir teste.robot
```
