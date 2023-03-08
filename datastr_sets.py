# Create an empty set

#in sets no more element will appear more than once insde of the set

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

#.remove() use to remove any values on the set
s.remove(2)
print(s)
#len will give you the length of everything

print(f"The set has {len(s)} elements")