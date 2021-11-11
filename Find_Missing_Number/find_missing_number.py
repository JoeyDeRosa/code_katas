def find_rune(a):
	uex = a
	op = ()
	for i in range(len(uex)):
		if i != 0:
			if uex[i] == '+' or uex[i] == '-' or uex[i] == '*':
				for x in range(len(uex)):
					if uex[x] == "=":
						op = (uex[i], i, x)
						break
				break
	for i in range(10):
		ex = uex.replace('?', str(i))
		if str(i) in uex:
			pass
		elif ex[0:op[1]] != str(int(ex[0:op[1]])) or ex[op[1] + 1:op[2]] != str(int(ex[op[1] + 1:op[2]])) or ex[op[2] + 1:] != str(int(ex[op[2] + 1:])):
			pass
		elif op[0] == '+':
			if int(ex[0:op[1]]) + int(ex[op[1] + 1:op[2]]) == int(ex[op[2] + 1:]):
				return(i)
		elif op[0] == '-':
			if int(ex[0:op[1]]) - int(ex[op[1] + 1:op[2]]) == int(ex[op[2] + 1:]):
				return(i)
		elif op[0] == '*':
			if int(ex[0:op[1]]) * int(ex[op[1] + 1:op[2]]) == int(ex[op[2] + 1:]):
				return(i)
	return(-1)

test = ["1+1=?", "123*45?=5?088", "-5?*-1=5?", "19--45=5?", "??*??=302?", "?*11=??", "??*1=??"]
for i in test:
	print(find_rune(i))