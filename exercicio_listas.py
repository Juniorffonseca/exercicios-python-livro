"""
Exercício 3.4
Criar uma lista com 3 convidados e fazer uma frase para cada um deles.
"""
lista = ['Naruto', 'Yugi', 'Lufi']

print('Gostaria de jantar comigo, ' + (lista[0]) + "?")
print('Gostaria de jantar comigo, ' + (lista[1]) + "?")
print('Gostaria de jantar comigo, ' + (lista[2]) + "?")
print('\n\tNaruto não poderá comparecer')


lista[0] = 'Sasuke'
print('\nGostaria de jantar comigo, ' + (lista[0]) + "?")
print('Gostaria de jantar comigo, ' + (lista[1]) + "?")
print('Gostaria de jantar comigo, ' + (lista[2]) + "?")
print('\n\tEncontrei uma mesa de jantar maior')


lista.insert(3, 'Goku')
lista.insert(4, 'Vegeta')
lista.append('Freeza')


print('\nGostaria de jantar comigo, ' + (lista[0]) + "?")
print('Gostaria de jantar comigo, ' + (lista[1]) + "?")
print('Gostaria de jantar comigo, ' + (lista[2]) + "?")
print('Gostaria de jantar comigo, ' + (lista[3]) + "?")
print('Gostaria de jantar comigo, ' + (lista[4]) + "?")
print('Gostaria de jantar comigo, ' + (lista[5]) + "?")
print('\n\tPosso convidar apenas duas pessoas para o jantar, a mesa maior não chegará a tempo')


convidado_removido1 = lista.pop()
convidado_removido2 = lista.pop()
convidado_removido3 = lista.pop()
convidado_removido4 = lista.pop()

print('\n' + convidado_removido1 + ', infelizmente você foi desconvidado')
print(convidado_removido2 + ', infelizmente você foi desconvidado')
print(convidado_removido3 + ', infelizmente você foi desconvidado')
print(convidado_removido4 + ', infelizmente você foi desconvidado')
print(lista[0] + ', Você continua convidado para o jantar')
print(lista[1] + ', Você continua convidado para o jantar')
del lista[0]
del lista[0]
print(lista)



