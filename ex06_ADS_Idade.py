#Nome: Fernando César Bertolo Júnior
#RA: 0298/22-1

ano_Nascimento = int(input('Digite o ano de nascimento: '))
ano_Atual = int(input('Digite o ano atual: '))
idade_Atual = ano_Atual - ano_Nascimento
idade1 = 2028 - ano_Nascimento
idade2 = 2050 - ano_Nascimento

print('Atualmente você tem: {} anos \nEm 2028 você terá: {} anos \nEm 2050 você terá: {} anos'.format(idade_Atual,idade1,idade2))
