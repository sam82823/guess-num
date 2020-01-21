import random
r = random.randint(1, 100)
count = 0
while True:
	count +=1 # count = count + 1
	ans = input('guess number: ')
	ans = int(ans)
	if ans == r:
		print('right number!')
		print('it is the', count, 'time')
		break
	elif ans < r:
		print('the number is bigger')
	elif ans > r:
		print('the number is smaller')
	print('it is the', count, 'time')