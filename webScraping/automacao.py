import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []
# atribuimos a resposta da requisicao a uma variavel chamada response
response = requests.get('https://g1.globo.com')

content = response.content

site = BeautifulSoup(content, 'html.parser')


# o find_all retorna uma lista com todos os elementos que atendem a condição
# no caso, todos os posts com a classe feed-post-body
post = site.find_all('div', attrs = {'class': 'feed-post-body'})

# nos nao conseguimos usa o text, quando usamos concatenadamento o findl_all
# apenas com estruturas de repetição
# print(post.text)

# neste exemplo, quase nao tivemos subtitulos

# tbm conseguimos acessar o link da notica, com o atributo HREF
# print(post.a['href'])


for item in post:
    #titulo
    titulo = item.find('a', attrs = {'class': 'feed-post-link'})
    # print(titulo['href'])
    #subtitulo
    subtitulo = item.find('div', attrs = {'class': 'feed-post-body-resumo'})

    if (subtitulo):
        # print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])

    else:
        lista_noticias.append([titulo.text, 'None', titulo['href'], ])


news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'link'])
print(news)
news.to_excel('noticias.xlsx', index=False)








 