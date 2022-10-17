*** Settings ***
Documentation        Keywords e Variaveis para ações gerais
Library        RequestsLibrary
Library        OperatingSystem


*** Variables ***
${response}

*** Keywords ***

Validar Status Code "${statuscode}"
    Should Be True             ${response.status_code} == ${statuscode}

Importar Json Estatico
    [Arguments]        ${nome_arquivo}
    ${arquivo}        Get File    ${EXECDIR}/jsons/${nome_arquivo}
    ${data}           Evaluate    json.loads('''${arquivo}''')    json
    [Return]          ${data}
