potions_rp = ['Great Mana Potion', 'Great Spirit Potion', 'Ultimate Spirit Potion']


for potion in potions_rp:
	print('Eu gosto de usar ' + potion.title())
print('\nTodas as pots são ótimas')


potions_rp_reais = potions_rp[:]


potions_rp.append('Supreme Spirit Potion')
print(potions_rp)
potions_rp_reais.append('Strong Mana Potion')
print(potions_rp_reais)



print('Minhas Potions favoritas são: ')
for potion in potions_rp:
	print(potion)


print('\nMinhas Potions favoritas reais são: ')
for potion in potions_rp_reais:
	print(potion)
