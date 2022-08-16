#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

print("==========================")
print("Converter Dias em Segundos")
print("==========================")

qntd_Dias = int(input("Digite quantos dias deseja converter em segundos: "))

# 60 * 24 = 1440 minutos em 24hr
# 60 * 1440 = 86.400 segundos em 24hr
valor_MinutosDIA = 60 * 24
valor_SegundosDIA = 60 * valor_MinutosDIA
converter = valor_SegundosDIA * qntd_Dias
print("{} dias convertidos em segundos = {} segundos".format(qntd_Dias, converter))





