import mysql.connector
con = ''
cursor = ''
try:
    # Criar conexão ao banco de dados #
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        database='python',
        password='root')

    # Declaração SQL a ser executada #
    criar_tabela_SQL = """CREATE TABLE produtos(
                             idproduto int(11) NOT NULL,
                             nomeproduto VARCHAR(70) NOT NULL,
                             preco DECIMAL(8,2) NOT NULL,
                             quantidade TINYINT NOT NULL,
                             PRIMARY KEY (idproduto))"""

    # Criar cursor e executar SQL no banco de dados #
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print('Tabela criada com sucesso!')

except mysql.connector.Error as erro:
    print(f'Falha ao criar tabela no MySQL: {erro}')

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada.')







