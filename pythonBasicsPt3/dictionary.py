
from cmath import pi


dict = {
    "name": "murali",
    "age": 24,
    "city": "chennai",
    "pi": 3.14
}

#methods in dictionary
#1.returns all the keys
print(dict.keys())

#return all values
print(dict.values())

#returns(key, value) pairs
print(dict.items())

#returns val according to key
print(dict.get("age"))

#adds new key value pair
dict.update({"food": "full meals"})
print(dict.items())