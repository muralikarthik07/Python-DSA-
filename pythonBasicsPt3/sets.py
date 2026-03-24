s = {1, 2, 3, 4, 5}
s.add(6)

print(type(s))

#adds value
s.add(6)

#removes a val
s.remove(6)

#empties the set
s.clear()

#s.pop() #removes a random element
s.pop()

#returns new union
s1 = {2,3,4,5,6}
s2 = {6,7,8,9,10}

print(s1.union(s2))

print(s1.intersection(s2))