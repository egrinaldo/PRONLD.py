print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_s = int(input("Digite o seu número: "))
    print ("Você digitou", chute_s)
    chute = int(chute_s)
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
      print("Você Acertou", "!!!!!Parabéns!!!!!")
    else:
         if(maior):
            print("Você Errou","!!!!!Não Foi Desta Vez!!!!!", "O seu numero foi maior. ")
         elif(menor):
            print("Você Errou","!!!!!Não Foi Desta Vez!!!!!", "O seu numero foi menor. ")

    rodada = rodada + 1


print("Fim de Jogo")