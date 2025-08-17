"""
Os loops são estruturas que permitem que um bloco de código seja executado repetidamente enquanto uma condição for verdadeira. 
- Loop for: Itera sobre uma sequência (como uma lista, string, ou intervalo) e executa um bloco de código para cada item dessa sequência.
"""

for i in range(10,15):
    print(i, end=' ')

print()

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta, end=' ')


print()
numeros = (10, 20, 30)
for numero in numeros:
    print(numero)

print()
texto = "python"
for letra in texto:
    print(letra)

print()

dados = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
for chave in dados:
    print(chave)

for valor in dados.values():
    print(valor)    


for chave, valor in dados.items():
    print(f"{chave}: {valor}")


lista = [11,5,8,10,60,80,90]

for i in lista:
    print(i)
    if i == 10:
        break #para o loop

for i in lista:
    if i >= 10 and i < 90:
        print(i)
        continue  #pula a condicao e continua


