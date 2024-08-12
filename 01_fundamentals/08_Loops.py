n=int(input("Enter a Number: "))

for i in range(1,11):
    print(n ,'*',i,'=',i*n)

print('*'*20)
for i in range(n,(n*10)+1,n):
    print(i)

print('*'*20)
#find probability of sum of digits on two dices

for n in range(1,13):
    number=0
    for i in range(1,7):
        for j in range(1,7):
            if(i+j==n):
                number+=1
    print(n,'=',round((number/6**2)*100,2))  

#enemurate in list
list=["Hello","How are You","I am fine"]              

for index,value in enumerate(list):
    print(f'index: {index}, value: {value}')

# List Comprehensions

square=[x**2 for x in range(5)]  
print(square)

#Armstrong number

def is_armstrong(num):
    numS=str(num)
    numLen=len(numS)

    
    newNum= sum(int(digit)**numLen for digit in numS)
    return newNum==num

num=int(input("Enter a number: "))
if(is_armstrong(num)):
    print("Yes armstrong")
else:
    print("Not Armstrong")    

#take input until user enter a negative number

number=[]

while True:
    user_input=input("Enter Number: ")

    if user_input.replace('.','',1).isdigit() and float(user_input)>0:
        number.append(float(user_input))
    elif user_input.replace('-','',1).replace('.','',1).isdigit() and float(user_input)<=0:
        break
    else:
        print("You have entered the invalid input")

print(f'The number entered are : {number}')