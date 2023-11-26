num=1
while num<=100:
	count = 0
	numb = 2
	while numb <= num // 2:
		if num % numb==0:
			count+=1
			break
		numb+=1
	if count==0 and num!=1:
		print(num)
	num +=1