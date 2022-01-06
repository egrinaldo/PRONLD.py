import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(0, 101)
total_de_tentativas = 0
pontos = 1000


print("Selecione O Seu nível de risco? ")
print("(1) Fácil (2) Médio(3) Difícil")

nivel = int(input("Define o nível: "))
if (nivel == 1):
  total_de_tentativas = 20
elif(nivel == 2):
  total_de_tentativas = 10
else:
  total_de_tentativas = 5


for rodada in  range (1,total_de_tentativas + 1):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_s = int(input("Digite o seu número entre 1 e 100: "))
    print ("Você digitou", chute_s)
    chute = int(chute_s)
    
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
      print("Você Acertou e você fez {}! ".format(pontos),  "!!!!!Parabéns!!!!!")
      break 
    else:
         if(maior):
            print("Você Errou","!!!!!Não Foi Desta Vez!!!!!", "O seu numero foi maior. ")
         elif(menor):
            print("Você Errou","!!!!!Não Foi Desta Vez!!!!!", "O seu numero foi menor. ")
         pontos_perdidos = abs(numero_secreto - chute)
         pontos = (pontos - pontos_perdidos)

    rodada = rodada + 1


print("Fim de Jogo")