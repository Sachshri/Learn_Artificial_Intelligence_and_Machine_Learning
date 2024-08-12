n=int(input("Enter the Number: "))
#if
if n>0 :
    print("This is Postive")
else:
    print("This is negative") 
#if elif
if n==0:
    print("this is zero")
elif n>0:     
    print("This is Postive")
else:
    print("This is negative")   

#if elif with logical operators

if n%5==0 and n%4==0:
    print("Divisible by 5 and 4 both")
elif n%5==0:
    print("Divisible by 5 only")    
elif n%4==0:
    print("divisible by 4 only")    
else: 
    print("Not divisible by 5 and 4 both")    


#Single line
i = 10
print(True) if i < 15 else print(False)

#Nested if else
num = 4
if num > 0:
    if num < 10:
    	print("The number is positive and less than 10.")
else:
    print("The number is less than or equal to 0")


#Print that a year is leap or not

year=int(input("Enter the year: "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(year," is a leap year")
else: 
    print(year, " is not a leap year")     