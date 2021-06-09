from random import randint  # use randint(a, b) to generate a random number between a and b\
number = randint(1,10)
print(number)

i=0

while number !=1:         
    i += 1  # i should be incremented by one each iteration
    number = randint(1,10)
         
if number == 1:
    print(f"The number of iterations are {i}")