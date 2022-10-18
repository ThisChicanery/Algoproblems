def caesarCipherEncryptor(string, key):
	a = list('abcdefghijklmnopqrstuvwxyz')
	string = list(string)
	b = []
	if key > 26:
		key = key - 26
	
	for i in range(len(string)):
		for j in range(len(a)):
			if string[i] == a[j]:
				if (j + key) >= 25:
					b.append(a[j+ key -26])
				else:
					b.append(a[j + key])
	b = ''.join(b)
    return b