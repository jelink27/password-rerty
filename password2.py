x = 3
while True:
	password = input('請輸入密碼：')
	if password =="aa":
		print('密碼正確')
		break
	else:
		x = x - 1
		if x > 0:
			print('密碼錯誤，還有' , x , '次機會')
		else:
			print('密碼錯誤太多次囉')
			break



'''
x = 3
while True:
	if x == 0:
		print('break')
		break
	elif x > 0:
		password = input('請輸入密碼：')
		if password == ('a123456'):
			break
		elif password !=('a123456'):
			print('密碼錯誤！還有' , x-1 , '次機會')
			x = x - 1

'''




'''
x = 3
while True:
	if x < 1:
		print('密碼錯誤，登入失敗')
		break
	password = input('請輸入密碼：')
	if password == ('a123456'):
		print('登入成功')
		break
	elif password !=('a123456') and x>= 1:
		x = x - 1
		print('密碼錯誤！還有' , x , '次機會')
'''		



'''
x = 3
while True:
	password = input('請輸入密碼：')
	if x <= 1 :
		break
	elif password ==('a123456'):
		print('登入成功')
		break
	elif password !=('a123456'):
		x = x - 1
		print('密碼錯誤！還有' , x , '次機會')

'''

'''
x = 3
while True:

	password = input('請輸入密碼：')
	if password ==('a123456'):
		print('登入成功')
		break
	elif password !=('a123456'):
		print('密碼錯誤！還有' , x , '次機會')
		x = x - 1
	if x <= 0:
		break
'''



'''		
	elif password !=('a123456'):
		x = x + 1
		print('密碼錯誤！還有' , x , '次機會')
	elif password !=('a123456'):
		x = x + 1
		print('密碼錯誤！還有' , x , '次機會')
'''
