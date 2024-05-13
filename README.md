# a3-tech-test

Para instalar todos os pacotes utilizados no projeto, abra seu terminal e digite pip install -r requirements.txt, se sua versão do python for a 3.12, use pip install -r requirements.txt --user.

Uma vez que todas as dependências estiverem instaladas, digite python -m uvicorn a3_tech_test.app.main:app --reload --host "0.0.0.0" --port "5000" --log-level INFO. Com isso, a aplicação estará ativa, só mandar requisições.

Caso VSCode seja sua IDE, instale as extensões Python, Python Debugger e então apenas aperte F5.

Para mandar as requisições, pode-se usar o Postman ou qualquer outra aplicação de sua preferência. Porém, você pode utilizar o arquivo test.py para testar as requisições.

O formato aceito pela API é o seguinte: 
{
    "query": "sua_query"
}

Seguem alguns exemplos de perguntas:
{
    "query": "Como parar de fumar?"
}

{
    "query": "Quais são as 5 principais características que definem uma pessoa como dependente de nicotina?"
}

{
    "query": "Quais são as perguntas sugeridas pela abordagem PAAPA?"
}

{
    "query": "O que é o PAAPA?"
}

{
    "query": "Como proceder com pacientes com esquizofrenia?"
}

{
    "query": "O que o protocolo diz sobre pacientes com tuberculose?"
}

{
    "query": "Explique o teste de Fagerstrom?"
}

{
    "query": "Quais sãos os problemas relacionaos à saude? Liste-os."
}

{
    "query": "O que é o PCDT? Explique detalhadamente."
}

{
    "query": "Quais os sintomas de privação que a ausência do tabaco provoca? Detalhe, por favor."
}

{
    "query": "O que fazer com casos de recaída de acordo com o protocolo do INCA?"
}