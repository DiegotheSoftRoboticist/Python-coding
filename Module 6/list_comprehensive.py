numbers = [1, 2, 3, 4 ,5]
doubled_numbers = []
 
for num in numbers:
	doubled_number = num*2
	doubled_numbers.append(doubled_number)

print(doubled_numbers)

doubled_numbers2 = [num * 2 for num in numbers]
 string_list = [str(num) for num in numbers]
#################################################################
friends = ["ashley","matt","michael"]

print([friend[0].upper() + friend[1:] for friend in friends])