import sqlite3
conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

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

conn.commit()

print("tabela criada com sucesso.")


