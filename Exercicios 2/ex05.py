#Nome: Fernando Bertolo Ra: 0298/22-1

primeira_Nota = float(input("Digite a primeira nota:"))
segunda_Nota = float(input("Digite a segunda nota:"))

media_Arit = (primeira_Nota + segunda_Nota) / 2
if(media_Arit >= 5):
    print("Media:", media_Arit)
    print("Parabens, Você foi aprovado")
else:
    print("Media:", media_Arit)
    print("Que pena, você foi reprovado")