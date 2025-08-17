# blocos de condicionais 



idade = int(input("idade:"))

if idade >= 18:
    renda = int(input("renda: "))
    if renda >= 2500:
        print("Aprovado.")
    elif renda < 2500:
        print(f"Falta o valor de R${2500 - renda},00 para ser aprovado.")
    else:
        print('Digite uma renda válida.')
elif idade < 18:
    print(f'Falta {18 - idade} anos para você conseguir aprovação.')
else:
    print("Digite uma idade válida por favor.")