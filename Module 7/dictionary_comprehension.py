numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}



str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}

instructor = dict(name="colt", city="san francisco", color="purple")
yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}

num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd") for num in num_list }

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
: