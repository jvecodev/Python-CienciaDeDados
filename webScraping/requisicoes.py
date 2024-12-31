import requests

# atribuimos a resposta da requisicao a uma variavel chamada response
response = requests.get('https://economize-ja2.vercel.app/home.html')

print(response.status_code) # 200
print("="*50)
print("Cabecalho da resposta: ")
print(response.headers) # retorna os headers da pagina
print("="*50)
print("Conteudo da resposta: ")
print(response.content) # retorna o conteudo da pagina


