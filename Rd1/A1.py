for X in range(int(input())):
	N = int(input())
	W = input()
	ans = ""
	arr = []
	for i in W:
		if i != 'F':
			arr.append(i)
	count = 0
	if len(arr)<=1:
		count = 0
	else:
		word = arr[0]
		for i in range(1, len(arr)):
			if arr[i] != word:
				count = count + 1
			word = arr[i]
	print("Case #"+str(X+1) + ": " + str(count))
