import sqlite3

# apontando qual arquivo vai ser utilizado e passando para uma nova variável
conexao = sqlite3.connect('Banco de Dados')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto)
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Sara","24","Engenharia Química")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"João","40","Administração")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Leticia","18","Medicina")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Alexandre","30","Marketing")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Gabriela","21","Direito")')
cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE nome="João"')

#3. Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos"
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for alunos in dados:
    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for alunos in dados:
    print(alunos)

#d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
total_alunos = dados.fetchone()[0]
print("Número total de alunos na tabela:", total_alunos)

#4. Atualização e Remoção:
#a) Atualize a idade de um aluno específico na tabela
cursor.execute('UPDATE alunos SET idade="35" WHERE nome="Gabriela"')

#b) Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos where id=3')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (1,"Vitoria","24","2.5")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (2,"Rodrigo","30","10.8")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (3,"Barbara","45","25.7")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (4,"Natalia","58","1.9")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (5,"Caroline","19","3.6")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (6,"Vinicius","26","9.0")')

#6 Consultas e Funções Agregadas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados_cliente = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
for clientes in dados_cliente:
    print(clientes)

#b) Calcule o saldo médio dos clientes.
dados_cliente = cursor.execute('SELECT AVG(saldo) FROM clientes')
for clientes in dados_cliente:
    print(clientes)

#c) Encontre o cliente com o saldo máximo.
dados_cliente = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
for clientes in dados_cliente:
    print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.
dados_cliente = cursor.execute('SELECT * FROM clientes WHERE saldo > 1000')
contador = 0
for cliente in dados_cliente:
    contador += 1

print("O número de clientes com saldo acima de 1000 é:", contador)

#7. Atualização e Remoção com Condições:
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo="100.5" WHERE nome="Natalia"')

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes where id=6')

#8. Junção de Tabelas:
#Crie uma tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real)
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(50), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

#Insira algumas compras associadas a clientes existentes na tabela "clientes".
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES (1,"Smartphone modelo X","10000.99")')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES (2,"Laptop modelo Z","2499.98")')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES (3,"Smartwatch  modelo Y","500.97")')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES (4,"Tablet modelo X","5000.95")')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES (5,"Fone de ouvido sem fiomodelo Y","200.99")')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
dados_compras = cursor.execute('SELECT nome, produto, valor FROM clientes LEFT JOIN compras ON clientes.id=compras.cliente_id')
for compras in dados_compras:
    print(compras)

#comandos para enviar e fechar a conexão
conexao.commit()
conexao.close()
