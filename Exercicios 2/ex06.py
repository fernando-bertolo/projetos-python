#Nome: Fernando Bertolo Ra: 0298/22-1

distCarro_A = float(input("Digite a distancia percorrida pelo carro A(em KM):"))
tempCarro_A = float(input("Digite o tempo levado para percorrer esta distancia:(em min)"))
distCarro_B = float(input("Digite a distancia percorrida pelo carro B(em KM):"))
tempCarro_B = float(input("Digite o tempo levado para percorrer esta distancia:(em min)"))

veloMedia_A = distCarro_A / tempCarro_A
veloMedia_B = distCarro_B / tempCarro_B

print("Velocidade media carro A: ", veloMedia_A)
print("Velocidade media carro B: ", veloMedia_B)

if(veloMedia_A > veloMedia_B):
    print("O carro A foi mais rapido")
else:
    print("O carro B foi mais rapido")