#年齡判定是否有駕駛資格
driving = input('是否有開過車: ')
if driving != '有' and driving != '沒有':
	print('請輸入有/沒有')
	raise SystemExit

age = input('請問年齡是多少? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('具有考照資格')
	else:
		print('尚未具備資格')
elif driving == '沒有':
	if age >= 18:
		print('有開車需要,請儘速考取駕照')
	else:
		print('未達車用駕駛年齡')

