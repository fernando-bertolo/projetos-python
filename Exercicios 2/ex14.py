#Nome: Fernando Bertolo Ra: 0298/22-1

resultado = 0

primeiroNumero = int(input("Digite o primeiro numero:"))
segundoNumero = int(input("Digite o segundo numero:"))
print(" 1 - Adição")
print(" 2 - Subtração")
print(" 3 - Multiplicação")
print(" 4 - Divisão")
op = int(input("Selecione uma das opções acima:"))


match op:
    case 1:
        resultado = primeiroNumero + segundoNumero
        print(primeiroNumero, "+", segundoNumero, " = ", resultado)
    case 2:
        resultado = primeiroNumero - segundoNumero
        print(primeiroNumero, "-", segundoNumero, " = ", resultado)
    case 3:
        resultado = primeiroNumero * segundoNumero
        print(primeiroNumero, "*", segundoNumero, " = ", resultado)
    case 4:
        resultado = primeiroNumero / segundoNumero
        print(primeiroNumero, "/", segundoNumero, " = ", resultado)


