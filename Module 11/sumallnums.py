def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total 

print(sum_all_nums(4,5,6,7,8,9,0))