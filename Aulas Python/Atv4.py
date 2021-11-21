def cal_Fat_(num):
    f = 1 
    for c in range(num , 0, -1):
     f *= c
    return f
num = int(input("Insira o Valor para o Cálculo: " ))
print (" O Resultado Fatorial é: " ,cal_Fat_(num))
