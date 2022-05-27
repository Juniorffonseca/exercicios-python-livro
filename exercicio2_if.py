current_users = ['user1', 'user2', 'user3', 'user4', 'admin']
new_users = ['user1', 'user2', 'user9', 'user10', 'admin2']


for user in new_users:
	if user.lower() in current_users:
		print('O nome de usuário ' + "'" + user + "'" + ' já está em uso, tente outro.')
	else:
		print('O nome de usuário ' + "'" + user + "'" + ' está disponível')




















"""if current_users:
	for usuario in current_users:
		if usuario == 'admin':
			print('Olá ' + usuario + ', gostaria de ver um relatório de status?')
		else:
			print('Olá ' + usuario + ', obrigado por fazer login novamente')


else:
	print('Precisamos encontrar alguns usuários')

"""
