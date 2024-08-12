#string is a collection or sequence of characters it is an immutable data structure 
#string concatenation using '+' 
string="    This is Sachin."
string2="this is sachin."
stringList=[string,string2]
concatenatedString=string + " " + string2
combined='***'.join(stringList)
print("combined",combined)
print(concatenatedString)
print('-'*20)
#string replication using *
print("Sachin"*3)

#string length
print(len(string))
print('*'*20)
#string slicing 
print(concatenatedString[5:9])
print(concatenatedString[-5:])
print(concatenatedString[-5:-1])
print(concatenatedString[:5])
print(concatenatedString[5:])
print('-'*20)
#Case Conversion
print(string.lower())
print(string.upper())

#string striping
print(concatenatedString.strip())
print(concatenatedString.lstrip())
print(concatenatedString.rstrip())
print("*"*20)
#string Replacing
print(concatenatedString.replace("Sachin","Shakti"))
print("*"*20)
#string Count
print(concatenatedString)
print(concatenatedString.count(' '))
print(concatenatedString.upper().count('S'))
print(concatenatedString.lower().count('s'))
print('*'*20)
#string find
print(concatenatedString.find('Sac'))
print('*'*20)

#string Formatting
#Default Order
String1="{}{}{}".format("Sachin ","Swati ","Shiv")
print(String1)

#According to the position Positional Formatting
String2="{2}{0}{1}".format("Sachin ","Swati ","Shiv")
print(String2)
#According to the Key
String3="{l}{m}{f}".format(l="Sachin ",f="Swati ",m="Shiv")
print(String3)
print('*'*20)
#Formatted String
keyword = 'example'
keyword_counts = {'example': 3}
print('The keyword "{}" appears {} times.'.format(keyword, keyword_counts[keyword]))

#formatted String literal
print(f'The keyword "{keyword}" appears {keyword_counts[keyword]} times.')

#other fomatting literals
print('The keyword "%s" appears %d times.' % (keyword, keyword_counts[keyword]))

#Reverse String
print("Hello"[::-1])
#s[::-1]: This slicing technique in Python starts from the end (-1) and moves backwards, effectively reversing the string. It reads the string from the last character to the first, creating a reversed version of the original string s.

##String Capitalization
print('my name is Sachin'.capitalize())
print('my name is Sachin'.title())
print("-" * 20)

#checking type of string
str='Sachin is best'
print(str.islower())
print(str.isupper())
print('123'.isdigit())
print(str.isalpha())
print(str.isascii())
print("*"* 20)
#start with end with
print(str.startswith('Sac'))
print(str.endswith('in'))
print("*"* 20)

#string adjustment
print(str.center(30,"-"))
print(str.ljust(30,"-"))
print(str.rjust(30,"-"))

#string split

newStr=str.split()
print(newStr)

names='''Sach"in's,Rahul,Robin,Gotam,Sourav'''
print(names.split(','))

#count the occurences of each unique word in the given string
given_str="This is Sachin. Today we are going to install the software which will help students to find jobs and study by their own way and make their progress faster without any teacher."

def find_all_occurences(str):
    words=str.split()
    unique_words=[]
    count_words=[]

    for word in words:
        if word in unique_words:
            index=unique_words.index(word)
            count_words[index]+=1
        else:
            unique_words.append(word)
            count_words.append(1)

    return unique_words,count_words


unique,count = find_all_occurences(given_str)

for i in range(len(unique)):
    print(unique[i],'->',count[i])