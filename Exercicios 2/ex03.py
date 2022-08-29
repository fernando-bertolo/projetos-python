#Nome: Fernando Bertolo Ra: 0298/22-1

ano_Atual = int(input("Digite o ano atual: "))
ano_Nasc = int(input("Digite o ano de nascimento: "))

idade = ano_Atual - ano_Nasc

if(idade < 18):
    print("Você é menor de idade, não pode entrar")
else:
    print("Você tem", idade, "anos, pode entrar na boate")