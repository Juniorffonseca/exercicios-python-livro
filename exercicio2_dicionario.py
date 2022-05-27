rios_paises = {
	'nilo': 'egito',
	'amazonas': 'brasil',
	'yangtze': 'china',
}


for rio, pais in rios_paises.items():
	print('\nO rio ' + rio.title() + ' corre pelo ' + pais.title() + '.')

print('\n\nOs rios contidos no dicionário são:')
for rio in rios_paises.keys():
	print('\n' + rio.title())

print('\n\nOs paises contidos no dicionário são:')
for pais in rios_paises.values():
	print('\n' + pais.title())
