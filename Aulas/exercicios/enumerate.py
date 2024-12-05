# frutas = ['maca','uva','banana','laranja']
# def  ordena_frutas (frutas):
#     for fruta in enumerate(frutas):
#         print(f"{fruta[0]}: {fruta[1]}")
# ordena_frutas(frutas)

# # exercicio2

# print ("----------------------------")

# numeros = [10, 20, 30, 40, 50, 60]

# #neste caso como eu estou acumulando valores, nao é uma boa opcao usar o list comprehension
# soma = 0

# for indice, valor in enumerate(numeros):
#     if indice % 2 == 0:
#         soma += valor  

# print(soma)

# # com list comprehension 

# numeros2 = [valor for indice, valor in enumerate(numeros) if indice % 2 == 0]
# # no dia a dia é melhor, porem nao utiliza a logica.
# soma = sum(numeros2)

# print(soma)


# #exercicio3 

# print("------------------------------")

# palavras = ['gato','cachorro','perereca','cavalo']

# def substituir_Palavras (palavras):
#     for indice, valor in enumerate(palavras):
#         if indice %2 != 0:
#             palavras[indice] = 'animal'
#     print(palavras)

# substituir_Palavras(palavras)


# print("------------------------------")

#exercicio4)

# cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]     

# def formatar_lista (cidades):
#     for indice, cidade in enumerate(cidades):
#         print(f'{indice + 1} - {cidade}')
# formatar_lista(cidades)


#exercicio5) palavras maiores que 7 letras

# palavras = ["Python", "enumerate", "prática", "função", "programação"]

# def palavras_maior_que_7 (palavras):
#     contador = 0
#     for indice, palavra in enumerate(palavras):
#         if len(palavra) > 7:
#             contador += 1
#             print(f'São os indices {indice + 1}')
#     print(f'São {contador} palavras com mais de 7 letras são os indice')

# palavras_maior_que_7 (palavras)

# lista1 = ["a", "b", "c"]
# lista2 = ["x", "y", "z"]
# lista = []

# def intercalar_listas(lista1, lista2, lista):
#     for indice, valor in enumerate(lista1):
#         lista.append(valor)
#         lista.append(lista2[indice])
#     for letra in lista:
#         print(letra, end = ' ')
# intercalar_listas(lista1, lista2, lista)


# alunos = ["Alice", "Bob", "Charlie", "Diana"]

# alunos_dict = {}

# for indice, valor in enumerate(alunos):
#     alunos_dict[indice] = valor
# print(alunos_dict)


# alunos = ["Alice", "Bob", "Charlie", "Diana"]

# # Criando o dicionário com dictionary comprehension
# alunos_dict = {indice: nome for indice, nome in enumerate(alunos)}

# print(alunos_dict)


#elementos multiplos de 3

# numeros = [5, 8, 12, 15, 18, 22, 24, 30, 35]
# numeros_multiplos = []

# for indice , valor in enumerate(numeros):
#     if valor %3 == 0:
#         numeros_multiplos.append(valor)


# print(f'Numeros multiplos de 3 {numeros_multiplos}')

#inverter ordem 
itens = ["caneta", "lápis", "borracha", "caderno", "mochila"]

for i, valor in enumerate(reversed(itens)):
    print(f"{len(itens) - 1 - i}: {valor}")

print('--------------------------------')

# Percorrer os índices de forma decrescente
                        #start,step,stop
for i in range(len(itens) - 1, -1, -1 ): 
    print(f"{i}: {itens[i]}")

#algumas atualizacoes



 



        






    




