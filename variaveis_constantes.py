primeiro_bi = float(input('Nota 1º Bi: '))
segundo_bi = float(input('Nota 2º Bi: '))
terceiro_bi = float(input('Nota 3º Bi: '))
quarto_bi = float(input('Nota 4º Bi: '))

media = ((primeiro_bi + segundo_bi + terceiro_bi + quarto_bi) / 4)

print (media)

if (media) >= 7:

    print ('Aprovado')

elif (media) >= 5:
    print ('Recuperação')

    media_recuperaçao = float(input('Nota da recuperação: '))

    print ('Média final: ') 
    print (float((media + media_recuperaçao) /2))

    if ((media + media_recuperaçao) /2) >=7:
        print ('aprovado')
    else:
        print ('reprovado')

else:
    print ('Reprovado')
    

