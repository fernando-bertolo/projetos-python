#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

qntd_Ap = int(input('Digite a quantidade de apartamento no hotel: '))
valor_Diaria = float(input("Digite o valor da diária no final de semana: "))
desconto = valor_Diaria * 0.25
valor_Promocional = valor_Diaria - desconto
print('O valor da diaria promocional é: R$', valor_Promocional)

valor_Total_100 = valor_Promocional * qntd_Ap
print('Total arrecadado caso a ocupação seja 100%: R$', valor_Total_100)

valor_70 = valor_Total_100 * 0.30
valor_Total_70 = valor_Total_100 - valor_70
print('Total arrecadado caso a ocupação seja 70%: R$', valor_Total_70)

total_SemDESC = valor_Diaria * qntd_Ap
preju = total_SemDESC - valor_Total_100
print("O hotel deixaria de ganhar R${} reais por conta da promoção".format(preju))
