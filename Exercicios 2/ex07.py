#Nome: Fernando Bertolo Ra: 0298/22-1

from datetime import date
ano_atual = date.today().year
print(ano_atual)

nomeP1 = input("Digite o nome da primeira pessoa:")
idadeP1 = int(input("Digite a idade da primeira pessoa:"))
nomeP2 = input("Digite o nome da segunda pessoa:")
idadeP2 = int(input("Digite a idade da segunda pessoa:"))

anoNascimentoP1 = ano_atual - idadeP1
anoNascimentoP2 = ano_atual - idadeP2

if(idadeP1 < idadeP2):
    print(nomeP1, "é mais novo(a), nasceu no ano de", anoNascimentoP1)
else:
    print(nomeP2, "é mais novo(a), nasceu no ano de", anoNascimentoP2)