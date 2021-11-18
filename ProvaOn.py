sala_A = 0
sala_B = 0
sala_C = 0
sala_D = 0
fim = 'sim'
total_A = 0
total_B = 0
total_C = 0
total_D = 0

while (fim != 'nao'):
    idade = float(input("Insira a Idade do Animal: "))
    castracao = float(input("Animal foi castrado: (Sim digite 0) (Não Digite 1):  "))
    sexo = float(input("Informe o Sexo do Animal: (MACHO digite 0) (FÊMEA Digite 1):  "))
    fivfelv = float(input("O Animal Possui FIVFELV: (Sim digite 0) (Não Digite 1) :  "))
    enc = float(input("Deseja Encerrar o Programa se SIM Digite 3: "))

    if (enc == 3):
        fim = 'nao'
    elif sala_A == sala_A and idade < 2 and castracao == 0 and castracao == 1 and sexo == 0 and sexo == 1 and fivfelv == 1:
         print ("Gato Alocado na SALA A : ")
         sala_A += 1
    elif sala_B == sala_B and idade > 2 and castracao == 0:
         print ("Gato Alocado na SALA B : ")
         sala_B += 1
    elif sala_C == sala_C and idade < 2 and idade > 2 and castracao == 1:
        print ("Gato Alocado na SALA C : ")
        sala_C += 1
    elif sala_D == sala_D and idade < 2 and idade > 2 and sexo == 0 and fivfelv == 0:
         print ("Gato Alocado na SALA D : ")
         sala_D += 1
    else:
         total_A = total_A + (sala_A)       
         total_B = total_B + (sala_B)
         total_C = total_C + (sala_C)
         total_D = total_D + (sala_D)
print ('Animais Totais na Sala A: ' ,total_A)
print ('Animais Totais na Sala A: ' ,total_B)
print ('Animais Totais na Sala A: ' ,total_C)
print ('Animais Totais na Sala A: ' ,total_D)


