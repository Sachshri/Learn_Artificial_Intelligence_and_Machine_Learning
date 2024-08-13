def fun1():
    print("My name is Sachin")
    return None
def greet(name):
    print("Hello",name)

def area(l,b):
    return l*b        

def perimeter(*args):
    return sum(args)    

def rectangle(**kwargs):
    sum=0
    for key,val in kwargs:
        sum+=kwargs[key]

    return sum

def cu(lst):
    return [v**3 for v in lst]

def sq(lst):
    return [v**2 for v in lst]

def final_sum(lst):
    c=cu(lst)
    s=sq(lst)

    return [c[i]+s[i] for i in range(len(lst))]

def reverse_list(numbers):
    return numbers[::-1]

def find_average(numbers):
    if __name__ == "__main__":
        # Code here will only run when the module is executed directly
        print("HEy buddy",reverse_list([2,4,5,7,9]))
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]
  
print(find_average({8888}))  