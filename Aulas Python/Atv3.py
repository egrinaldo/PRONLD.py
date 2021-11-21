def val_in (val1,val2,val3):
    if (val1 > val3 and val3 < val2):
        return val1,val2,val3
    elif (val1 > val2 and val3 > val2):
        return val1,val3,val2
    elif (val2 > val1 and val3 < val1):
        return val2,val1,val3
    elif (val2 > val3 and val3 > val1):
        return val2,val3,val1
    elif (val3 > val1 and val2 < val1):
        return val3,val1,val2
    elif (val3 > val2 and val2 > val1):
        return val3,val2,val1
val1 = int(input("Informe o Primeiro valor: "))
val2 = int(input("Informe o Segundo  valor: "))
val3 = int(input("Informe o Terceiro valor: "))
print ("A Ordem Crescente dos Valores São", val_in(val1,val2,val3))