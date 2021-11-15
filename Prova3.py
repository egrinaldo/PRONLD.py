nome = str(input("Informe Seu Nome: "))
cpf = float(input("Informe seu CPF: "))
vl_pago= 'sim'
total = 0
while (vl_pago != 'nao'):
    prod = float(input('Insira o valor do Produto:  (Para encerrar a compra Digite 0) '))
    if (prod == 0):
        vl_pago = 'nao'
    else:
        total = total + (prod)
        print ("Total a Ser PAGO: " ,total)
        if total < 200: 
            print ("Obrigado Por Comprar Conosco")
            print ("Valor do Frete: R$ 19.90")
            print ("Total a ser Pago: " , total + 19.90)
        else:
            total > 200
            print ("Obrigado Por Comprar Conosco")
            print ("Você Ganhou Frete Grátis")
            print ("Total a ser Pago: " , total)
print (nome)
print (cpf)
print ("Total a ser Pago: " ,total)
print ("Volte Sempre!")