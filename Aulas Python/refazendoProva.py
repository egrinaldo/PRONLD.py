from random import randrange
nome = ''
compra = ''
cpf = []
clientes = []
telefone = []
finalizar = 0
total = 0

while compra != 'fim':
    compra = float(input('Informe o valor do produto: ' 'Para Finalizar Digite 0: '))
    
    if (compra == 0):
        finalizar != 'nao'
        nome = input('Informe o nome do cliente: ')
        telefone = int(input('Insira o Número de Telefone: '))
        cpf = int(input('Insira o CPF: '))
        if compra > 200:
           print ("\nObrigado Por Comprar Conosco\n")
           print ("Você Ganhou Frete Grátis")
           print ("Total a ser Pago: " , total)
    else:
        total = total + (compra)

