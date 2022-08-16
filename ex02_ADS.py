#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

horas_Trabalhadas = float(input('Digite as horas trabalhadas no mes: '))
valor_HoraTrabalhada = int(input('Digite o valor da hora trabalhada: '))
percentual_Desconto = float(input('Digite o percentual de desconto: '))

salario_Bruto = horas_Trabalhadas * valor_HoraTrabalhada
total_Desconto = (percentual_Desconto/100) * salario_Bruto
salario_Liquido = salario_Bruto - total_Desconto

print('Horas trabalhadas: {} \n Salario Bruto: {} \n Desconto: {} \n Salario Liquido: {} '.format(horas_Trabalhadas, salario_Bruto, total_Desconto, salario_Liquido))
#print('Salário Bruto: {}'.format(salario_Bruto))
#print('Desconto: {}'.format(total_Desconto))
#print('Salario Liquido: {}'.format(salario_Liquido))