lst=[30,45,78,"sachin",True]
print(lst)
print("*"*20)
#Accessing List
print(lst[4])

for i in lst: 
    print(i,end=' ')
print()

for i in range(len(lst)):
    print(lst[i],end=' ')
print()

for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=' ')
print()

for i in range(-1,-(len(lst)+1),-1):
    print(lst[i],end=' ')
print()
print('*'*20)
#slicing list
print(lst[-4])
print(lst[2:5])
print(lst[-4:-1])
print(lst[-5:-1])

print('*'*20)
#modifying list
lst[4]="Rahul"
print(lst)
print('*'*20)
#adding elements

lst.append('6')
lst.append('Rahul')
print(lst)

lst.extend(["Gotam","Sanjana","Priyanka"])
print(lst)
print("-"*20)

#adding element at specified position
lst.insert(4,"banana")
print("After insetion to specified position",lst)

#removing elements
lst.remove("sachin")
print(lst)
print(lst.pop())#return the last element and pop out last
print(lst)
print("Remove from specified postion")
print(lst.pop(2))
print(lst)
del lst[3]
print(lst)
print('-'*20)

#Count a specific element
print(lst.count("Rahul"))
print('-'*20)

#index
print(lst.index('Gotam'))
print('-'*20)
# print(lst.index('sachin')) give value error

#concatenatin
lst2=[5,7,8,9,4,77]
print(lst+lst2)
print("-"*20)

#sorting
lst2.sort(reverse=True)
print(lst2)
#reversing
lst2.reverse()
print(lst2)

#max and min
print(max(lst2))
print(min(lst2))
print("*"*20)

#Do the above operation all for multidimensional array

#list Comprehension
arr=[i for i in range(1,6)]
print(arr)

arr=[i**2 for i in arr]

matrix=[[i for i in range(5)] for j in range(5)]
print("matrix",matrix)
#create array of even numbers
even=[i for i in range(1,21) if i%2==0]
print("Even: ",even)
#flattening a multidimensional list
array=[[1,2,3],[4,5,6],[7,8,9]]
print(array)

flattened=[element for row in array for element in row]
print(flattened)

#Searching in array
element=5
position=[(i,row.index(element)) for i,row in enumerate(array) if element in row]
print (position)


#Find the maximum element in the list 
maximum=float("-inf")

for row in array:
    maximum=max(maximum,max(row))

print(maximum)

#make a list which contain prime numbers in given range
Range=int(input("Enter the Range: "))
primes=[]
def is_prime(num):
    if num<2:
        return False
    else:
        for j in range(2,int(num**0.5)+1):
            if(num%j)==0:
                return False    
    return True        



prime=[i for i in range(2,Range) if is_prime(i)]
# for i in range(2,Range):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#             break
#     if count==0 :
#         primes.append(i)    

print(prime)    