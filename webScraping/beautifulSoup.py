import requests
from bs4 import BeautifulSoup
# atribuimos a resposta da requisicao a uma variavel chamada response
response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# prettify() é um método que melhora a visualização do código
# com indentação e quebras de linha
# print(site.prettify())

#o tipo do site é um objeto do tipo BeautifulSoup, assim conseguimos manipular o site
# print(type(site))

# podemos acessar as tags do site como se fosse um dicionário

post = site.find('div', attrs = {'class': 'feed-post-body'})

# como ja temos a variavel post, podemos acessar as tags filhas dela
# sabemos que é o titulo do post 

title = post.find('a', attrs = {'class': 'feed-post-link'})

# dest meneira imprimimos o texto junto com a tag completa 

print(title)

# dessa maneira imprimimos apenas o texto
print(' =v= '* 10)

print(title.text)

print(' =v= '* 10)
# print(post.prettify())

#subtitle 

subtitulo = post.find('div', attrs = {'class': 'feed-post-body-resumo'})

print(subtitulo.text)

 