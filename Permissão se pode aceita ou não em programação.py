try:
    idade = int(input("Digite a idade"))
except:
    print("A idade precisa de um número!")
if idade>= 18:
 print("Acesso permitido")
else:
     print("Acesso negado")