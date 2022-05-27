sebastiao = {
	'tipo': 'gato',
	'dono': 'junior',
	}

kyuubi = {
	'tipo': 'jinchuriki',
	'dono': 'naruto',
	}

susanoo = {
	'tipo': 'jinchuriki',
	'dono': 'sasuke',
	}


pets = [sebastiao, kyuubi, susanoo]


for pet in pets:
	print('Tipo de pet: ' + pet['tipo'].title())
	print('Dono do pet: ' + pet['dono'].title() + '\n')
