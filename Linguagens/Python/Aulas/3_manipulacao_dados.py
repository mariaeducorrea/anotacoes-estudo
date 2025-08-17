print("Manupulações com números")
a = 10
b = 5

#numeros complexos
z1 = 1 + 2j
z2 = 2 - 3j

print(a + b)  # soma
print(a - b)  # subtração
print(a * b)  # multiplicação
print(a ** b)  # multiplicação inteira
print(a / b)  # divisão
print(a // b)  # divisão inteira

print(z1 + z2)  # soma
print(z1 * z2)  # multiplicação
print(z1.real)  # acesso a parte real
print(z1.imag)  # acesso a parte imaginária



print('--------------------------')
print("Manupulações com texto")
nome = "João"
sobrenome = "Silva"
texto = "Python"
nome = "Maria" 
idade = 25
print(nome + " " + sobrenome)  
print(nome * 3) 
print(texto.upper())  # PYTHON
print(texto.lower())  # python
print(texto.replace("P", "J"))  # Jython
print(texto.split("t"))  # ['Py', 'hon']
print(texto[0])      # P
print(texto[1:4])    # yth
print(texto[-1])     # n
#verificações do texto 
print(texto.isalpha())    # False (contém números)
print(texto.isdigit())    # False (não é só número)
print(texto.isalnum())    # True (letras e números)
print(texto.startswith("Py"))  # True
print(texto.endswith("3"))     # True

# Formatação com f-strings (recomendado)
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Método format()
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Antigo (%)
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))


print('--------------------------')
print("Manupulações com booleanos")
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False



print('--------------------------')
print("Manupulações com sequencias")

lista = [1, 2, 3, 4, 5, 6]
lista.append(4)    # adicionadno
lista.insert(1, 5) # inserindo em um local especifico
lista.remove(2)    # removendo
lista.sort()       # Ordena em ordem crescente
lista.reverse()    # Ordena em ordem decrescente
frase = "Aprender Python é divertido"
palavras = frase.split()  # ["Aprender", "Python", "é", "divertido"]
csv = "nome,idade,cidade"
dados = csv.split(",")    # ["nome", "idade", "cidade"]

print(len(lista))  # Conta quant. elementos da lista
print(lista[1])     # 5
print(lista[1:3])   # [5, 3]
print(palavras)
print(dados)



print('--------------------------')
print("Manupulações com tuplas (tuplas são imutáveis)")
tupla = (1, 2, 3)
print(tupla[1])    # 2



print('--------------------------')
print("Manupulações com mapeamento/dicionariso chave:valor")
dados = {"nome": "João", "idade":30}
print(dados)
dados["cidade"] = "POA"
print(dados)
print(dados["nome"])
del dados["idade"]
print(dados)

print(dados.keys()) 
print(dados.values())
print(dados.items())
