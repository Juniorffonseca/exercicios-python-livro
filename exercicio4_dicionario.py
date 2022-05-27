pessoa1 = {
	'first name': 'Junior',
	'last name': 'Fonseca',
	'age': '21',
	'city': 'sp',
	}

pessoa2 = {
	'first name': 'Naruto',
	'last name': 'Uzumaki',
	'age': '17',
	'city': 'konoha',
	}

pessoa3 = {
	'first name': 'Sasuke',
	'last name': 'Uchiha',
	'age': '18',
	'city': 'konoha',
	}

people = [pessoa1, pessoa2, pessoa3]


for pp in people:
	nome_completo = pp['first name'] + ' ' + pp['last name']
	primeiro_nome = pp['first name']
	ultimo_nome = pp['last name']
	idade = pp['age']
	cidade = pp['city'].title()
	print('\nNome Completo: ' + nome_completo.title())
	print('Primeiro Nome: ' + primeiro_nome.title())
	print('Ultimo Nome: ' + ultimo_nome.title())
	print('Idade: ' + idade)
	print('Cidade: ' + cidade.title())
	
