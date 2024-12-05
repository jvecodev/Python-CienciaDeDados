# funcao lambda
# utilizado para criar anonimas de maneira simples e compacta 
# Variavel = Argumentos:expressao
# muitas vezes usado com reduce, map ou filter 


# numeros = [1,2,3,4,5]

# potencia = lambda indice:indice ** 2

# #o map recebe primeiro a codicao depois o iteravel 
# lista_potencia = list(map(potencia, numeros))
# print(lista_potencia)

#exercicio lambda 

palavras = ['casa', 'computador', 'mesa', 'janela', 'carro', 'sol']

tamanho = lambda palavra: len(palavra) < 5

listaNova = list(filter(tamanho, palavras))

print(listaNova)

# outra maneira mais resumida 


palavras = ['casa', 'computador', 'mesa', 'janela', 'carro', 'sol']

palavras_filtradas = list(filter(lambda palavra: len(palavra) < 5, palavras))

print(palavras_filtradas)

print(' ------------------------------- ')


usuarios = [('Ana', 25), ('João', 20), ('Carlos', 30), ('Beatriz', 22)]

ordenar = lambda x : x[0]

listaNova = sorted(usuarios, key = ordenar)

print(listaNova)

print(' ------------------------------- ')

#divisiveis por 3 

numeros = [10, 15, 20, 25, 30, 35, 40]

ordenar = lambda numero: numero % 3 == 0

numeros_Novos = list(filter(ordenar, numeros))


print(numeros_Novos)

print('mesmo resultado porem o exemplo a baixo é um pouco mais limpo e eficiente')

numeros_novo2 = list(filter(lambda numero1 :numero1 % 3 == 0, numeros))

print(numeros_novo2)














