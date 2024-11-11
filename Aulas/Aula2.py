
# fatorial
a = int(input('Digite o numero para calcular o fatorial: '))

def fatorial(a):
    total = 1
    while a > 1:
        total *= a
        a -= 1
    print(total)

fatorial(a)



