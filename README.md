# a3-tech-test

Teste técnico para a A3Data.

O teste consiste na criação de um assistente usando RAG (Retrieval Augumented Generation) com o intuito de responder à perguntas de médicos sobre um protocolo disponibilizado pelo INCA(Instituto Nacional de Câncer).

## Instalação

1. Clone o repositório
2. Instale os pacotes com pip install -r requirements.txt ou pip install -r requirements.txt --user.
2.1. Se preferir, pode instalar via setup.py, apenas utilizando o comando pip install .
2.2. Ou ainda, pode utilizar a imagem docker disponível, para fazer o build use o comando docker build -t sua_tag ., em seguida use docker run -d -p 8080:90 --name nome_do_container sua_tag. Se estiver usando a imagem docker, pule o passo seguinte.
3. Para executar o projeto, cole o seguinte comando em seu terminal: python -m uvicorn a3_tech_test.app.main:app --reload --host "0.0.0.0" --port "5000" --log-level trace
4. Para mandar as requisições, pode-se usar o Postman ou qualquer outra aplicação de sua preferência. Porém, você pode utilizar o arquivo test.py para testar as requisições. O formato aceito pela API é o seguinte: 
{
    "query": "sua_query"
}

5. Exemplo de perguntas:
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