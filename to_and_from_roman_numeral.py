def to_numeral(a):
	num = str(a)[::-1]
	rn = ''
	key = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M', 'M')]
	count = 0
	for i in num:
		if count < 3:
			if int(i) < 4:
				for x in range(int(i)):
					rn += key[count][0]
			elif int(i) == 4:
				rn += (key[count][1] + key[count][0])		
			elif int(i) != 9:
				for x in range(int(i) - 5):
					rn += key[count][0]
				rn += key[count][1]
			else:
				rn += (key[count + 1][0] + key[count][0])
			count += 1
		else:
			for x in range(int(i)):
				rn += "M"
	return(rn[::-1])

	

test = to_numeral(2309)
test1 = to_numeral(57)
test2 = to_numeral(4044)

print(test, test1, test2)

def from_numeral(a):
	rn = a
	num = 0
	key = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
	for i in range(len(rn) - 1):
		if key[rn[i]] < key[rn[i + 1]]:
			num -= key[rn[i]]
		else:
			num += key[rn[i]]
	num += key[rn[-1]]
	return(num)



test = from_numeral('MMCMIV')
test1 = from_numeral('CDXLIV')
test2 = from_numeral('CMXCIX')

print(test, test1, test2)