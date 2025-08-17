"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = 1
y = 2
z = x + y
s1 = "eai"
s2 = ", tudo certo?"
resposta1 = True
resposta2 = False
altura = 1.55
lista = ['banana', 67, 'maça']
tuplas = (1, "seila", "##" )
intervalo = range(5,10)
dicionario = {
    'nome':'maria',
    'altura': 1.55,
    'seila': 'nao sei'
}


print(x+y)
print(type(z)) #verificar tipo de dado
print(type(s1 + s2))
print(type(resposta1),type(resposta2))
print(type(altura))
print(lista,type(list)) #Lista mutável
print(tuplas,type(tuplas) ) #ista imutável
print(intervalo,type(intervalo))
for i in intervalo:
    print(i, end=' ') #mostrar e formato de linha e não em baixo do outro3
    
print("\n",dicionario) #\n para pular linha


