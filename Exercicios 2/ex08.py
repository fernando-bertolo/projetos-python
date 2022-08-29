#Nome: Fernando Bertolo Ra: 0298/22-1

notaP1 = float(input("Digite a primeira nota:"))
notaP2 = float(input("Digite a segunda nota:"))

media = (notaP1 + notaP2) / 2
mediaExame = 10 - media

if(media >= 7):
    print("Você tirou", media, "e foi aprovado")
elif(media >= 4 and media < 7):
    print("Você tirou", media, "e esta de exame")
    print("Você precisa tirar", mediaExame,"na proxima prova")
else:
    print("Você tirou", media, "e foi reprovado")


