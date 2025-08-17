"""
Isso é feito utilizando blocos try, except, mas existem outros comandos relacionados a isso, como else, finally e até mesmo a geração de erros com raise.
"""

#try:
    #o código que pode gerar erro
#except:
    #o código para tratar o erro

def pergunta_idade():
    try: 
        idade = int(input("idade: "))
        print(idade)
        if idade >= 18:
            print("liberado")
        else:
            print('Não liberado')
    except ValueError:
        print('Valor inválido.')

pergunta_idade()

''''
Tipos de exceções 

- ValueError: Quando uma função recebe um argumento de tipo correto, mas com valor inadequado (ex.: tentando converter uma string não numérica em um número).
- ZeroDivisionError: Quando ocorre uma divisão por zero.
- TypeError: Quando uma operação ou função é aplicada a um objeto de tipo incorreto.
- IndexError: Quando se tenta acessar um índice de uma lista ou sequência que não existe.
- FileNotFoundError: Quando um arquivo não pode ser encontrado no sistema.
- KeyError: Quando se tenta acessar uma chave inexistente em um dicionário.
'''

'''
Quando Usar o Tratamento de Erros?
Use o tratamento de exceções quando você sabe que uma operação pode falhar de forma previsível, e você deseja tratá-la de maneira controlada. Por exemplo, ao tentar acessar um arquivo, ao fazer uma conversão de tipo, ou ao dividir números.

Quando Não Usar o Tratamento de Erros?
Não é recomendado usar o tratamento de exceções em casos onde você pode prever facilmente o erro e resolvê-lo de outra maneira. Em vez disso, você deve tratar a causa do erro diretamente.

'''