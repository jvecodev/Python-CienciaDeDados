# #enumerate

lista = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(lista):
    print(i)

print('---------------------')
# desta maneira eu printo apenas os indices
lista2  = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(lista2):
    print(i[1])

# print('---------------------')
# # desta maneira eu printo apenas os valores
# lista3  = ['a', 'b', 'c', 'd', 'e']
# for i in enumerate(lista3):
#     print(i[1])


# def verificarSTR(valor):
#     if type(valor) is str:
#         print(f'{valor} é uma string')
#     else:
#         tipo = type(valor)
#         print(f'{tipo} este é o tipo do valor')

#     return valor

# numero = 1
# letra = 'a'

# verificarSTR(letra)


# intercalando valores
# valores = [1,2,3,4,5]
# letras = ['a','b','c','d','f']
# listaIntercalada = []
# def intercalando_valores(valores, letras, listaIntercalada):
#     for i in range (len(valores)):
#         listaIntercalada.append(valores[i])
#         listaIntercalada.append(letras[i])
#     print('Listas intercaladas →', listaIntercalada)

# intercalando_valores(valores, letras, listaIntercalada)

# Aqui eu conectei a posicao da listaCarros, junto com a posicao da listaPreco sem usar o len, usando o enumarate e um for

listaCarros = ["Nissan", "Toyota", "Ford", "Chevrolet"]
listaPrecos = [1000, 2000, 3000, 4000]

def relacionar_carro_preco(Carros, Precos):
    for i, carros in enumerate(Carros):
        print(f"Este carro {carros} vale {Precos[i]}")

relacionar_carro_preco(listaCarros, listaPrecos)