Diego = {
	"Name" : "Diego",
	"Family Name" :"Higueras-Ruiz",
	"Age" : 29,
	"Is cute" : False,
}

Diego2 = dict (Name = "Diego",  FamilyName = "Higueras-Ruiz")

Diego["Name"] # Access to the information in a Dictionary

for value in Diego.values():
	print(value)

for key in Diego.keys():
	print(key) 

for key,value in Diego.items():
    print(key,value) 

"address" in Diego #False

d = dict(a=1,b=2,c=3)
d.clear()
d # {}

d = dict(a=1,b=2,c=3)
c = d.copy()
c # {'a': 1, 'b': 2, 'c': 3}
c is d # False

{}.fromkeys("a","b") # {'a': 'b'}
dict.fromkeys(["email"], 'unknown') # {'email': 'unknown'}
{}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}

d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1
d['b'] # 2
d.get('b') # 2
d['no_key'] # KeyError
d.get('no_key') # None

d = dict(a=1,b=2,c=3)
d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
d # {'c': 3, 'b': 2}
d.pop('e') # KeyError

d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() # ('d', 4)
d.popitem('a') # TypeError: popitem() takes no arguments (1 given)


first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}
second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# let's overwrite an existng key
second['a'] = "AMAZING"
# if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# the update overrides our values
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


