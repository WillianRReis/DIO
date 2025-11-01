def exibir_mensagem():
    print ('Olá mundo!')

def exibir_mensagem_2(nome):
    print (f'Seja bem vindo {nome}!')

def exibir_mensagem_3(nome='Reis'):
    print (f'Seja bem vindo {nome}!')

exibir_mensagem()
exibir_mensagem_2('Will')
exibir_mensagem_3()


def salvar_carros(marca, modelo, ano):
    print (f'Carro inserido com sucesso! {marca} / {modelo} / {ano}')

salvar_carros (marca=(str(input('Inseir marca: '))), modelo=(str(input('Inserir modelo: '))), ano=(int(input('Inserir ano: '))))





