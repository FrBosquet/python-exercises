print('Intenta adivinar el numero!')

secret = 2
guess = int(input('Cual crees que es? '))

if guess == secret:
	print('Acertaste!!!!!')
else:
	print('Fallaste!!!')