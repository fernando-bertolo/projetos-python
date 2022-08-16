#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

salario_Minimo = float(input("Digite o valor do salario minimo: "))
qntd_Kw = float(input("Digite a quantidade de Kw consumida: "))
custo_Kw = salario_Minimo * 0.20
print("O valor a ser pago por cada Kw é: R${}".format(custo_Kw))

valor_total = custo_Kw * qntd_Kw
print("O valor total a ser pago é: R${}".format(valor_total))

desconto = valor_total * 0.15
valor_total_DESC = valor_total - desconto
print("O valor total com desconto é: R${}".format(valor_total_DESC))