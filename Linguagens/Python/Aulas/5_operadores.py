#operadores aritmeticos

#Adição
a = 10
b = 5
print(a + b)  # 15

#Subtração
print(a - b)  # 5

#Multiplicação
print(a * b)  # 50

#Divisão
print(a / b)  # 2.0

#Divisão inteira
print(a // b)  # 2

#Modulo
print(a % b)  # 0

#Exponenciação 
print(a ** 2)  # 100 (10²)

#Operadores Unários
# Operador unário negativo
negativo = -a
print(negativo)  # -10

# Operador unário positivo (não altera o valor)
positivo = +a
print(positivo)  # 10





#operadores logicos

# and
x = 5
y = 10
print(x > 3 and y < 20)
print(x > 6 and y < 20)
print(x > 3 or y > 20)  
print(x > 6 or y > 20) 

# not
print(not x > 3)  
print(not x < 3)

#in e not in
frutas = ["maçã", "banana", "laranja"]
print("maçã" in frutas)
print("maçã" not in frutas)

x = 5
y = 10
z = 15
print(x > 3 and not y > 20 or z == 15)





#operadores de comparação

# Maior que (>):
print(5 > 3)  # True

# Menor que (<):
print(2 < 5)  # True

# Maior ou igual (>=):
print(5 >= 5)  # True

# Menor ou igual (<=):
print(3 <= 4)  # True

# Igual a (==):
print(10 == 10)  # True

# Diferente de (!=):
print(10 != 5)  # True


# Uso em outros tipos de dados

# Strings: Comparações são baseadas na ordem lexicográfica (alfabética).
print("apple" < "banana")  # True
print("apple" == "Apple")  # False (case-sensitive)

# Listas e Tuplas: Comparação elemento por elemento.
print([1, 2, 3] < [1, 2, 4])  # True
print((1, 2) == (1, 2))       # True
