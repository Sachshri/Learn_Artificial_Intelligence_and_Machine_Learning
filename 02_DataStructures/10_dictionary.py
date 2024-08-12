dct={1: "Sachin","shiv":"shakti"}
print(dct)
#creation of a dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Data', 2: 'Science', 3: 'Python'})
print("Dictionary with the use of dict() method: ")
print(Dict)

Dict = dict([(1, 'Data'), (2, 'Science')])
print("Dictionary with each item as a pair: ")
print(Dict)

#Accessing Elements of Dictionary
# To access a value in a dictionary, you can use square brackets [] and provide the key. If the key is not present in the dictionary, it will raise a KeyError. To avoid this, you can use the get method
my_dict = {'name':'Rose', 'age': 24}
print(my_dict['name'])  
print(my_dict['age'])   
print(my_dict.get('name','Unknown'))
print(my_dict.get('city','Unknown'))

#modifying values 
dct["Ram"]="Shyam"

dct[8]="Sachin"
print(dct)
print(dct[8])
print(dct.get(8))

#Deleting an element
del dct[8]
print(dct.pop(1))
print("2"*20,Dict.popitem())
print(dct)
#Accessing all the elements 
for k,v in dct.items():
    print(k,v)
print("*"*50)
for k in dct.keys():
    print(k,dct[k])

for v in dct.values():
    print(v)    
dct1={5: "Ramayan",7:"Ghanshyam"}
dct2={1: "krishna",2:"Shiv",3:"Ram"}
dct3={"Rama":5}
dct1.update(dct2)
print(dct1)

dct3["Shuma"]=dct3.get("shyam",0) + 1
print(dct3)
#find the frequency of each word in the sentence

def word_frequency_counter(sentence):
    word_list = sentence.split()
    word_counts = dict()

    for word in word_list:
      word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

user_sentence = input("Enter a sentence: ")

word_frequencies = word_frequency_counter(user_sentence)
print("Word frequencies in the sentence:")
for word, count in word_frequencies.items():
    print(word, count)

if(3 in dct2.keys()):
    print("Yes")

#Multidimensional Dictionary

multi_dict={
    1:{"info":{"name": "Sachin","fname":"ShriNiwas"},"marks":{"hin":"5","eng":"50","phy":"100"},"address":{"h.no":"6960","city":"panipat","state":"Haryana","country":"india"}},
    2:{"info":{"name": "Sahiil","fname":"Gotam"},"marks":{"hin":"59","eng":"80","phy":"100"},"address":{"h.no":"690","city":"karnal","state":"Haryana","country":"india"}}
} 

for k in multi_dict.keys():
    print(k,multi_dict[k]["address"])

#Use Case 
#Find the occurence of each word in the corpus

corpus=[
    "This is the multidimensional dictionary.",
    "This dictionary stores the sub dictionary.",
    "And this is the third containing the word and count.",
    "Is this the first level of dictionary?"
]

def find_occurences(corpus):
    word_freq={}

    for document in corpus:
        words=document.split()

        for word in words:
            if word not in word_freq:
                word_freq[word]={"Total Count":1,"documents":{document:1}}
            else:
                word_freq[word]["Total Count"]+=1
                if document in word_freq[word]["documents"]:
                    word_freq[word]["documents"][document]+=1
                else:
                    word_freq[word]["documents"][document]= 1  

    return word_freq

word_frequencies=find_occurences(corpus)
for word, info in word_frequencies.items():
    print(f"Word: {word}")
    print(f"  Total Count: {info['Total Count']}")
    print("  Document Occurrences:")
    for document, count in info['documents'].items():
        print(f"    {document}: {count}")
    print()

    #Dictionary Comprehension
    D1={i:i*i for i in range(1,11)}
    print(D1)
    D2={i:i**3 for i in range(1,11) if i%2==0}
    print(D2)
    
    #dictionary from list
    lt=[5,6,78,9,3]
    D3={lt.index(i):i for i in lt}
    print(D3)
    print("="*60)
    #Nested Dictionary
    D4={
        k1:{k2: k1*k2 for k2 in range(5,10)} for k1 in range(7,15)
    }
    print(D4)

    #find the common elements from the given list 
    lst1=[1,23,4,6,4]
    lst2=[1,2,4,6,4,9]
    lst3=[18,23,4,6,6]
    lists=[lst1,lst2,lst3]
    def findCommon(lists):
        common_freq={element:(lst.count(element)) for lst in lists for element in set.intersection(*map(set,lists))}
        return common_freq
    common_freq=findCommon(lists)
    for element,freq in common_freq.items():
        print("Element:",element,"Frequency:",freq)