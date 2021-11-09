def w2n(a):
	word = a.replace('-', ' ')
	word = word.split(' ')
	num = 0
	pnum = 0
	key = {	"ze": 0,
			"on": 1,
			"tw": 2,
			"th": 3,
			"fo": 4,
			"fi": 5,
			"si": 6,
			"se": 7,
			"ei": 8,
			"ni": 9,
			"ten": 10,
			"eleven": 11,
			"twelve": 12,
			"hundred": 100,
			"thousand": 1000,
			"million": 1000000, }
	for i in word:
		print(i)
		if i == 'ten' or i == 'eleven' or i == 'twelve':
			pnum += key[i]
		elif i == 'hundred' or i == 'thousand' or i == 'million':
			pnum *= key[i]
			if i != 'hundred':
				num += pnum
				pnum = 0
		elif i[-2:] == 'ty':
			pnum += (key[i[0:2]] * 10)
		elif i[-4:] == 'teen':
            pnum += (key[i[0:2]] + 10)
		elif i != 'and':
			pnum += key[i[0:2]]
	num += pnum
	return(num)
