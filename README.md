
Projeto Interdisciplinar IV 

O projeto foi feito em node.js, javascript, HTML, CSS, Python e SQlite3

Integrantes do grupo
Ian Freitag

Pedro Esteves Paselar

João Pedro Fortes Pachêco Pinheiro Correia


Intuito do projeto
Um pagina com o intuito de fazer uma visualização de dados com os dados dos veículos anunciados na WebMotors.

Execução do código
1. Para a executar o Banco de dados
Executar os seguintes scripts SQL:

A. criação da tabela:

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_veiculo(
    idVeiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    idunico INT NOT NULL,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    versao_veic TEXT NOT NULL,
    valor_veic FLOAT NOT NULL,
    ano_veic INT NOT NULL,
    ano_frab INT NOT NULL,
    carroceria TEXT NOT NULL,
    km_veic FLOAT NOT NULL,
    cor TEXT NOT NULL,
    vendedor TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL
)
""")

2.Para executar a raspagem:
Verificar se o banco foi criado antes de executar a raspagem

Executar o arquivo requisicao.py


3.Para executar a página:
Executar o comando  "node app.js"  no terminal