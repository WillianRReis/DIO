#
#texto = "Willian"

#print (texto.upper())


#print ("-".join(texto))#


nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
curso = str(input('Digite seu curso: '))

#print ("Olá, me chamo {nome}, tenho {idade} anos e estou matriculado no curso de {curso}"
#       .format(nome=nome, idade=idade, curso=curso))

print (f"Olá, me chamo {nome}, tenho {idade} anos e estou matriculado no curso de {curso}")