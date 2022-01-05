nome = str(input("Informe Seu Nome: "))
cpf = float(input("Informe seu CPF: "))
total = 0
fim = True


while True:
    prod = float(input('\nInsira o valor do Produto:  (Para encerrar a compra Digite 0) \n'))
    if (prod == 0):
        break
        
        
    else:
        total = total + (prod)
        
        if total < 200 : 
        
           print ("\nFrete Grátis em Compras Acima de R$ 200 \n")
           print ('Valor do frete R$ 19,90')
           print (nome)
           print (cpf)
           print ("Valor Total do Carrinho: " , total + 19.90)
        else:
            total > 200
            print ("\nVocê Ganhou Frete Grátis !!!\n")
            print (nome)
            print (cpf)
            print ("Valor Total do Carrinho: " , total)
            
print ("\nObrigado Por Comprar Conosco!\n")

