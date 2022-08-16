print('=====================')
print('     Calculadora     ')
print('=====================')
contador = 0
while contador == 0:

    primeiro_Numero = int(input('Digite o primeiro numero:'))
    segundo_Numero = int(input('Digite o segundo numero: '))

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    operacao = input('Escolha qual operacao deseja:')

    match int(operacao):
        case 1:
            soma = (primeiro_Numero) + (segundo_Numero)
            print(primeiro_Numero, "+", segundo_Numero,"=", soma)
        case 2:
            subtracao = primeiro_Numero - segundo_Numero
            print(primeiro_Numero, "-", segundo_Numero, "=", subtracao)
        case 3:
            multiplicacao = primeiro_Numero * segundo_Numero
            print(primeiro_Numero, "*", segundo_Numero, "=", multiplicacao)
        case 4:
            if (primeiro_Numero == 0 or segundo_Numero == 0):
                print("Não existe divisao por zero")
                resposta = input("\nDeseja fazer a operação denovo? (S/N)\n")
                if(resposta == "n" or resposta == "N"):
                    contador = 1
                else:
                    contador = 0
            else:
                divisao = primeiro_Numero / segundo_Numero
                print(primeiro_Numero, "/", segundo_Numero, "=", divisao)
        case _:
            print("\nSelecione uma opção válida")
            resposta = input("\nDeseja fazer a operação denovo? (S/N)\n")
            if(resposta == "n" or resposta == "N"):
                contador = 1
            else:
                contador = 0









