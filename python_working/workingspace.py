x = "kala"
print(x)

value = "string"
print(value[0])
value = "stringvalue"           #slice value in string
slicevalue = slice(2,6)       
print(value[slicevalue])#[2:6]

listvalue = ["hello","i","am","python"]         #slice value in list
slicevalue = slice(1,len(listvalue))
print(listvalue[slicevalue])

letter = ["rama","kala","suri","tara","zaina","zala"]      #case sensetive upper and lower case
inputvalue = input("Enter Your Word Here : ").lower()
for value in letter:
    if inputvalue in value:
        print(value)

letter = "helloworld"
print(letter.isupper())
a = input("Enter name ")
print("hello "+ a)

a="apple"
for i in a:
    print(i)

word = input().lower()             # Palindrome in string
reverse = ""
for i in word:
    reverse = i + reverse
if reverse == word:
    print(reverse)
else:
    print(f"This is not a Palindrome word: {word}")
    print("This is not a Palindrome word :" + word)


word = ["car","mom","level","home"]          #Palindrome in list
reverse = []
for i in word:
    if i == i[::-1]:
        reverse.append(i)
    print("This is a Palindrome word :",reverse)
else:
    print(f"This is not a Palindrome word : {word}")

dictionary_value = {
    'name' : 'tara',
    'age' : '21',
    'city' : 'chennai',
}
print(dictionary_value.keys())           # print only keys
print(dictionary_value.values())         # print only values
dictionary_value['skill'] = 'python'     # add key and value in dictionary
print(dictionary_value)
dictionary_value['city'] = 'Bangalore'   # update value in dictionary
print(dictionary_value)
remove_key = dictionary_value.pop('city')   
print(remove_key)                        # remove value. o/p is show which value is removed
print(dictionary_value)                  # remove value through the key. o/p is shown the remaining key/values in the dictionary

set_add = {"a","b","c","d"}
set_add.add("e")                           #set in add
print(set_add)

set_value = {1,22,3,44}
set_value2 = {"orange","kala"}             #set in update
set_value.update(set_value2)
print(set_value)

set_union = {11,12,13,14,15}
set_union2 = {16,17,18,13,14}
set_union3 = set_union|(set_union2)
set_union4 = set_union-set_union2
set_union5 = set_union & set_union2
set_union6 = set_union ^ set_union2
print(set_union3)                            #set in union
print(set_union4)                            #set in difference
print(set_union5)                            #set in intersection
print(set_union6)                            #set in symmetric difference

tuple_value = ("apple","banana","cherry","mango")
to_list = list(tuple_value)
to_list[2] = "kiwi"                            #tuple in add .append() .remove()
tuple_value = tuple(to_list)
print(tuple_value)

value = int(input())
list_value = ["kala","tara","zaina"]       #index position using list input
print(list_value[value])

value = input("Enter Your key : ")
dictionary_value = {
    'name' : 'tara',
    'age' : '18',
    'city' : 'chennai'
}
print(dictionary_value.get(value))

dictionary_value = {
    'name' : 'tara',
    'age' : '18',                   #key'th index position in dictionary
    'city' : 'chennai'
}
convert_list = list(dictionary_value.keys())
input_value = input("Enter Your Key : ")
index = convert_list.index(input_value)
print(f"Index of key is : {index}" )

value = int(input("Enter Your Index : "))
tuple_value = ("apple",12,27,"hello")           #index position in tuple
print(tuple_value[value])

value = int(input("Enter Your Index : "))
set_value = {"rama","12","rambo","24"}            #index position in sets. this is unordered so the result vary every time run the program
set_list = list(set_value)
print(set_list[value])