contatos = {
    'Will': {'nome': 'Will', 'idade': 40, 'cidade': 'GRU'},
    'Joao': {'nome': 'Joao', 'idade': 41, 'cidade': 'REC'},
    'Luiz': {'nome': 'Luiz', 'idade': 42, 'cidade': 'JPA'},
    'Eder': {'nome': 'Eder', 'idade': 43, 'cidade': 'SSA'},
    }

for chave, valor in contatos.items():
   print (chave, valor)

print (contatos.get ('Carlos', 'Não Existe'))

nomes = contatos.keys ()
cidades = contatos.keys ()
print (nomes)
print (cidades)


dados = {'nome':'Ian', 'idade': 20, 'cidade':'BSB'}
print (dados.keys())

removido = contatos.pop ('Joao')

print (contatos)
print (removido)
print (contatos.values())

inclusao = {'nome': 'Andre', 'idade': 44, 'cidade': 'POA'}
contatos.update (inclusao)
print (contatos)

