favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}


pessoas = ['jen', 'phil', 'will', 'vini', 'biel', 'manu', 'edward', 'sarah']


for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")


for pessoa in pessoas:
	if pessoa in favorite_languages.keys():
		print('Obrigado por responder a enquete, ' + pessoa.title() + '.')
	else:
		print('Por favor responda a enquente, ' + pessoa.title() + '.')
	
