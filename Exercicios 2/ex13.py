#Nome: Fernando Bertolo Ra: 0298/22-1

numero = int(input("Digite valores númericos entre 0 e 5:"))
resposta = input("Você deseja numerais em ingles ou portugues? (P/I)")
if(resposta == "P" or resposta == "p"):
    match numero:
        case 0:
            print("Zero")
        case 1:
            print("Um")
        case 2:
            print("Dois")
        case 3:
            print("Tres")
        case 4:
            print("Quatro")
        case 5:
            print("Cinco")
else:
    match numero:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
