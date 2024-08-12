#Tuple are ordered pair which are not mutable and can have duplicate values
tuple=((3,5),(6,7),(8,9),(3,5))
print(tuple)

#Accessing
tup=(1,3,5,6)
print(tup[2])

#Slicing
print(tup[2:4])

#concatination
print(tuple+tup)

print(tup.count(4))
print(len(tup))
print(tup.index(4))
print(tup*4)