caminho = 'C:\Users\jccol\OneDrive\estudos\Python-CienciaDeDados\Aulas\LeiturArquivo\PibMunicipios.txt'

with open(caminho) as arquivo:
    f_data = arquivo.readlines()
    

linhas = []

print(f_data)
        