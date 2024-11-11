lista = [j  for j in range (51)]

print(lista) 
print('Para não escrever os primeiros 50 termos')

def filtra_primos(lista):
    lista_primo = [n for n in lista if n > 1 and all(n % i != 0 for i in range(2, n))]
    print(lista_primo)
    return lista_primo

filtra_primos(lista)

