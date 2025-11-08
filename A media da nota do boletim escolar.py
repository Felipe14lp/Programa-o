try:
    media = int(input("Digite a media: "))
except:
    print("A media precisa de um numero!")
if media>= 7:
 print("Aprovado")
else:
        print("Reprovado")
