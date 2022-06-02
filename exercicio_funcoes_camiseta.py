# 8.3 - Camiseta: Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. 
# A função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem estampada. Chame a função uma vez usando argumentos posicionais para criar uma camiseta. 
# Chame a função uma segunda vez usando argumentos nomeados.


# Criando a função 'make_shirt()'
def make_shirt(tamanho, texto):
    print(str(tamanho) + ' ' + str(texto))

# Chamando a função uma vez usando argumentos posicionais
make_shirt('G', 'Testando')

# Chamando a função novamente, porém usando argumentos nomeados
make_shirt(tamanho='G', texto='Testando')


# 8.4 - Camisetas grandes: Modifique a função make_shirt() de modo que as camisetas sejam grandes por default, com uma mensagem Eu amo Python. 
# Crie uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem diferente.

# Modificando a função make_shirt() 
def make_shirt(tamanho = 'G', texto = 'Eu amo Python'):
    print(str(tamanho) + ' ' + str(texto))

# Criando as camisetas que o exercício pede
make_shirt()
make_shirt(tamanho = 'M')
make_shirt(tamanho = 'P', texto = 'Qualquer texto')

# 8.5 - Cidades: Escreva uma função chamada describe_city() que aceite o nome de uma cidade e seu país. 
# A função deve exibir uma frase simples, como Reykjavik está localizada na Islândia. 
# Forneça um valor default ao parâmetro que representa o país. Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default.

# Escrevendo a função chamada describe_city
def descibre_city(cidade, pais = 'Brasil'):
    print(cidade + " está localizada no " + pais)
# Chamando a função das formas que o exercício pede
descibre_city('São Paulo')
descibre_city('Rio de janeiro')
descibre_city('Tokyo', 'Japão')
