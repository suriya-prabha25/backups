import re
# text = "jesus is the only a king"
# message = re.search("[^a-z]",text)
# print (bool(message))

# def character_check(text):
#     message = re.search(r'[^a-zA-Z0-9]',text)
#     return bool(message)
# print(character_check("absSDFGH12"))

# text = "the real god"
# message = re.findall("z.*g",text)
# if message:
#     print(message)
# else:
#     print("Not matched")

# def word_matches(string):
#     message = re.search("[^a.le$]",string)
#     if message:
#         return not bool(message)
#     else:
#         return 'Word is not found'
# print(word_matches('a good apple'))

# def string_start(string):
#     result = re.findall("\w$",string)
#     if result:
#         return result
#     else:
#         return 'not matched'
# print(string_start('& My god is brave'))

# def start_end(word):
#     result = re.search("\Bz\B",word)
#     if result:
#         return result
#     else:
#         return 'not matched'
# print(start_end('he is very lazy'))


# def text_match(text):
#     patterns = '\w*z\w*'
#     if re.search(patterns,  text):                  #first
#       return text
#     else:
#       return('Not matched!')
# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("Python Exercises."))

# def text_match(text):
#   word = re.search("\w*\Bz\B\w*",text)     #\w*z\w*
#   if word:
#     return word                                  #second
#   else:
#     return 'not matched'

# print(text_match("The quick brown fox jumps over thelazy dog."))
# print(text_match("Python Exercises nzmccv aaahfdsh duye."))

# def alphanumeric_underscore(string):
#   text = re.search("^\d.\w*\s\w*$",string)
#   if text:
#     return text
#   else:
#     return "String Not Found"
# print(alphanumeric_underscore("jesusisThe8King 9"))
# print(alphanumeric_underscore("8helloim4suriya 6"))
# print(alphanumeric_underscore("4suriya prabha"))

# string_with_whitespace = "  Hello , i am suriya prabha  "
# store = ""
# space_store = ""
# for i in string_with_whitespace:
#   if (not i.isspace()):
#     store+=i
#   else:
#     space_store+=i
    
# print(store)
# print(space_store)



# result = "".join(string_with_whitespace.split())
# print(result)

# Add leading zero's to a number in python
# number = 7
# range_number = 6
# number_to_string = str(number).zfill(range_number)
# print(number_to_string)

# string_num = input("Enter Your of a Number Here : ")
# string_value = len(string_num)
# value = int(input("Enter Your Range of a Number Here : "))
# final_result = (-(string_value - value))
# # for i in range(value):
# if(final_result > 0): 
#   result = "0"*final_result + string_num                #"{range_num}".join(string_num)
#   print("Added Leading Zeros : " + result)            
          
# string_num = len("56656")
# value = (20)
# print(string_num)
# print(value)
# final_result = (-(string_num - value))
# print(final_result)


class Animal:
  def soundd(self):
    print("Animal makes sound")


class Dog(Animal):
  def sounds(self):
    print("Dog Bark")

class Bird(Dog):
  def sound(self):
    print("Bird Sing")
a1 = Bird()
a1.sounds()