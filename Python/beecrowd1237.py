def substringCompare(string1, string2):
	for indexout in range(len(string2)):
		if indexout == 0 and string1 == string2:
			return len(string2)
		substringLength = len(string2) - indexout
		compareRange = len(string2) - substringLength
		for indexin in range(compareRange+1):
			substring = string2[indexin:indexin+substringLength]
			if substring in string1:
				return substringLength
	return 0

while True:
	try:
		string1 = input()
		string2 = input()
		print(substringCompare(string1, string2))
	except EOFError:
		break