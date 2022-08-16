#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

pesoUM = 2
pesoDOIS = 3
pesoTRES = 5

primeira_Nota = int(input('Digite a primeira nota: '))
segunda_Nota = int(input('Digite a segunda nota: '))
terceira_Nota = int(input('Digite a terceira nota: '))

media_Ponderada = ((primeira_Nota * pesoUM) + (segunda_Nota * pesoDOIS) + (terceira_Nota * pesoTRES)) / (pesoUM + pesoDOIS + pesoTRES)

print(media_Ponderada)
