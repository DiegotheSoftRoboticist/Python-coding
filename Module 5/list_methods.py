alphabet = ["a","b","c"]
print(alphabet)
alphabet.append("d")
print(alphabet)
alphabet.extend(["d","Diego",5])
print(alphabet)
alphabet.insert(1,"d")
print(alphabet)
alphabet.clear
print(alphabet)
alphabet = ["a","b","c"]
print(alphabet)
alphabet.pop(2)
print(alphabet)
alphabet.remove("b")
print(alphabet)
print(alphabet.index("a"))
alphabet = ["a","b","c","a"]
print(alphabet.index("a",1)) #tells you the index of "a" afte the first index
print(alphabet.count("a"))
alphabet.reverse()
print(alphabet)
alphabet.sort()
print(alphabet)
alphabet = ["a","b","c","a","f","d","g","h","j","n","m","z"]
#print("These are the letters I know ".join(alphabet)) # string methods to create strings from lists

#slicing
print(alphabet[1:7])
print(alphabet[1:7:2])
print(alphabet[1::2])
print(alphabet[1::-1])
alphabet[1:3] = [1,1,1,1,1,1]
print(alphabet)

#Swapping Values

alphabet[1], alphabet[2] = alphabet[2], alphabet[1]