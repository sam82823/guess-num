import random
r = random.randint(1, 100)
while True:
	ans = input('guess number: ')
	ans = int(ans)
	if ans == r:
		print('right number!')
		break
	elif ans < r:
		print('the number is bigger')
	elif ans > r:
		print('the number is smaller')