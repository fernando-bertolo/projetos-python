#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

idade = int(input("Digite a sua idade: "))
idade_Mes = int(input("Digite quantos meses passou desde o seu ultimo aniversario: "))
idade_Dias = int((input("Digite quantos dias passou desde o começo do mes: ")))
idade_Segundos = (idade * 31536000) + (idade_Mes * 2592000) + (idade_Dias * 86400)

print("Você tem {} anos {} meses e {} dias \n Sua idade em segundos é: {}".format(idade,idade_Mes,idade_Dias, idade_Segundos))




#idade_Mes = idade * 12
#idade_Dias = idade * 365
#idade_Segundos = idade * 31536000
#print("Sua idade: {} anos \nSua idade em meses: {} meses \nSua idade em dias: {} dias \nSua idade em segundos: {} segundos".format(idade,idade_Mes,idade_Dias,idade_Segundos))
