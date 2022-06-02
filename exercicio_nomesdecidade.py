# 8.6 Nomes de cidade: Escreva uma função chamada city_country() que aceite o nome de uma cidade e seu país. A função deve devolver uma string formatada assim:
# "Santiago, Chile"
# Chame sua função com pelo menos três pares cidade-país e apresente o valor devolvido.

# Criando a função
def city_country(cidade, pais):
    print(cidade.title() + ', ' + pais.title())

# Chamando 3 vezes, conforme o exercicio pede
city_country('Santiago', 'Chile')
city_country('São Paulo', 'Brasil')
city_country('Pernambuco', 'Brasil')

# 8.7 Álbum: Escreva uma função chamada 'make_album()' que construa um dicionário descrevendo um álbum musical. 
# A função deve aceitar o nome de uma artista e o título de um álbum e deve devolver um dicionário contendo essas duas informações.

# Escrevendo a função
def make_album(nome, titulo):
    album = {'nome': nome, 'titulo': titulo}
    return album.title()

teste = make_album('xama', 'malvadao')
print(teste)
teste2 = make_album('imagine dragons', 'enemy')
print(teste2)
teste3 = make_album('alok', 'eletronicas')
print(teste3)