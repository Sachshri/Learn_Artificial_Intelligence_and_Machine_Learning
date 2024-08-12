#set is a data structue mutable unordered unique element using {} in python
my_set={2,1,3,4,4}
print(len(my_set))

#adding 
my_set.add(8)
print(my_set)
print("-"*20)

#popping
print(my_set.pop())
print(my_set)

#Removing
print(my_set.discard(3))
print(my_set)

#update
my_set.update((5,6,6,7))
print("Updated",my_set)
#iterating
for v in my_set:
    print(v)


#checking value in set or not
print(8 in my_set)

#set operations
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

print(set.intersection(set1,set2))
print(set.union(set1,set2))
print(set.difference(set1,set2))
print(set.isdisjoint)
print(set.issubset(set1-set2,set1))
print(set.remove)
