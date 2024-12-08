listaPalavra = ['p','a','y','a','t','h', 'o','n']

def removerA(lista):
    contador = 0
    for valor in lista:
        if valor == 'a' or valor == 'A':
            contador += 1
            lista.remove(valor)
    print(f'quantidade de letra {contador}')
    print(lista)

removerA(listaPalavra)


#crie uma lista que contenha apenas os numeos impares de 1 a 51


listaImpares = [i for i in range(1,52) if i % 2 != 0]
print(listaImpares)


# agora com lambda 

ordenar = lambda numeros: (numeros % 2 != 0) 
listaImpares2 = [ordenar(indice) for indice in range (1,52)]
print(listaImpares2)

# relacionar duas listas

lista1 = [1,2,3,4,5,6]
lista2 = ['a','b','c','d','f','g']

def mesclarListas(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3

print(mesclarListas(lista1, lista2))


# agora mesclando dicionarios

dicionario1 = {'a':1, 'b':2, 'c':3}
dicionario2 = {'d':4, 'e':5, 'f':6}

def mesclarDicionarios(dicionario1, dicionario2):
    dicionario3 = {}
    for chave, valor in dicionario1.items():
        dicionario3[chave] = valor
    for chave, valor in dicionario2.items():
        dicionario3[chave] = valor
    return dicionario3

print(mesclarDicionarios(dicionario1, dicionario2))




    