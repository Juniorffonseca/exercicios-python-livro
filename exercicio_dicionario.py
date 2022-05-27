dicionario = {
	'Cobra Sword ': 'Scarlet',
	'Gnome Sword ': 'Gnome bosses',
	'Lion wand': 'Drume',
	'Falcon Longsword': 'oberon',
	'Pendulet amulet': 'Faceless bane',
}



for termo, significado in dicionario.items():
	print('\nLoot: ' + termo.title())
	print('Boss: ' + significado.title())
