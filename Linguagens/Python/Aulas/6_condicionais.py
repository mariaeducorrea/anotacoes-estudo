# if, else, elif
'''
if condição1:
    # Bloco de código se a condição1 for verdadeira
elif condição2:
    # Bloco de código se a condição2 for verdadeira
else:
    # Bloco de código se todas as condições forem falsas
'''

idade = int(input("Idade: "))

if idade >= 18:
    print("Liberado")
elif idade < 18:
    print("Não Liberado")
else:
    print("Digite uma idade válida.")