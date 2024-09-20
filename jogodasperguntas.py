pontuacao = 0

print('Bem vindo ao jogo das perguntas')

#Primeira pergunta
resposta = input('Qual a capital da França? ') 
if resposta.lower() == 'paris':
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!")

    #Segunda pergunta 

    resposta = input('Quantos mundiais o Palmeiras tem? ')
    if resposta.lower () == '0':
        print("Correto")
        pontuacao += 1
    else:
        print("Errado")

    #Terceira pergunta
    resposta = input('Qual o maior time do mundo? ')
    if resposta.lower () == 'Corinthians':
        print("Correto")
        pontuacao += 1
    else:
        print("Errado")

        print(f"Sua pontuação final é {pontuacao} de 3 perguntas")

