#lambda
lst=[5,6,7,8,3,2,5]
sq=lambda x:x**2 
print(sq(8))

#lambda on list
sq_lst=[(lambda x: x**2)(x)for x in lst]
print(sq_lst)

#zip
zipped=zip(sq_lst,lst)
print(dict(zipped))

print(list(zip(lst,sq_lst)))

# unzipippid
# sq,val=zip(*zipped)
# print(sq)
# print(val)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)

#Filter

even=list(filter(lambda x: x%2==0,lst))
print(even)

#map
odd=list(map((lambda x: x%2==1),lst))
print(odd)

#use zip to find transpose

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(list(x for x in zip(*matrix)))
