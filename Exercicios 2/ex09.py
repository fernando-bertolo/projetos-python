#Nome: Fernando Bertolo Ra: 0298/22-1

# SalarioFinal = valorFixo + %sobre vendas
# 0 a 1500 -> 2%
# 1501 a 3000 -> 3%
# 3001 a 6000 -> 5%
# +6001 -> 6%
# descontado 5 reais a cada dia de falta

salario = 0
salarioFinal = 0

valorFixo = int(input("Digite o valor da parte fixa do salario:"))
vendas = float(input("Digite o total de vendas do mes: (em reais)"))
qntdFalta = int(input("Quantas faltas você teve no mes?"))

if(vendas >= 0 and vendas <= 1500):
    salario = vendas * 0.02

elif(vendas >= 1501 and vendas <= 3000):
    salario = vendas * 0.03

elif(vendas >= 3001 and vendas <= 6000):
    salario = vendas * 0.05

else:
    salario = vendas * 0.06


falta = qntdFalta * 5
salarioFinal = valorFixo + salario
salarioFinal = salarioFinal - falta
print("Salario Final:", salarioFinal)





