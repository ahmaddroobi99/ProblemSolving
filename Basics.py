str1 = "AhmAdDRRdagknmffjkblverkmfbmekfbmJEMDFIBJMEKRJMB"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower + upper)
print("arranging characters giving precedence to lowercase letters:")
print(sorted_string)


def findDigitsCharsSymbols(inputString):
    charCount = 0
    digitCount = 0
    symbolCount = 0
    for char in inputString:
        if char.islower() or char.isupper():
            charCount += 1
        elif char.isnumeric():
            digitCount += 1
        else:
            symbolCount += 1

    print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)


inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")

findDigitsCharsSymbols(inputString)


def mixString(s1, s2):
    s2 = s2[::-1]
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    length = lengthS1 if lengthS1 > lengthS2 else lengthS2
    resultString = ""
    for i in range(length):
        if (i < lengthS1):
            resultString = resultString + s1[i]
        if (i < lengthS2):
            resultString = resultString + s2[i]

    print(resultString)


s1 = "Abc"
s2 = "Xyz"
mixString(s1, s2)


def stringBalanceCheck(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)



str1 = "Emma25 is Data scientist50 and  ahmad 99AI Expert"
print("The original string is : " + str1)

# Words with both alphabets and (numbers)
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

res = []
temp = str1.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)



print (print("ahamd"))


# Exercise to reverse each word  of a string
def reverse_words(Sentence):
    # Split string on whitespace
    words = Sentence.split(" ")

    # iterate list and reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]

    # Joining the new list of words
    res_str = " ".join(new_word_list)
    return res_str


# Given String
str1 = "ahamd droobi99 gmail .com "
print(reverse_words(str1))



with open('sample.text', 'r') as file:
    data = file.read().replace('\n', ' ')
    print(data)



number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
# get list's size
n = len(number_list)
# iterate list till i is smaller than n
while i < n:
    # check if number is greater than 50
    if number_list[i] > 50:
        # delete current index from list
        del number_list[i]
        # reduce the list size
        n = n - 1
    else:
        # move to next item
        i = i + 1
print(number_list)




number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(number_list) - 1, -1, -1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)



list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# modify item
list1[1][3] = 3500
# print final result
print(list1)



emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}
print(emp_dict['company']['employee']['payable']['increment'])


listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at even-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)


#
# sampleList = [34, 54, 67, 89, 11, 43, 94]
#
# print("Original list ", sampleList)
# element = sampleList.pop(4)
# print("List After removing element at index 4 ", sampleList)
#
# sampleList.insert(2, element)
# print("List after Adding element at index 2 ", sampleList)
#
# sampleList.append(element)
# print("List after Adding element at last ", sampleList)


ar =[1,2,3,4,56,7,8]


print (ar)

temp = ar.pop(3)

print(ar )

ar.insert(2,temp)

print(ar)

#ar.append(temp)   #

ar.insert(len(ar)-1,temp)
print (ar)

# reverse 3 slices from array
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]


slice =int (len(sampleList)/3)

s1 =sampleList[0:slice]

print("first slice :" +str(s1))
print("first slice reversed :" +str(s1[::-1]))


s2=sampleList[slice :slice*2]

print("second slice :" +str(s2))
print("second slice reversed :" +str(s2[::-1]))


s3 =sampleList[slice*2:slice*3]

print("third slice :" +str(s3))
print("third slice reversed :" +str(s3[::-1]))





#Exercise 4: Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element



sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(sampleList)
dictCount= dict()
for i in sampleList:
    if (i in dictCount )  :
        dictCount[i]+=1
    else:
        dictCount[i]=1


print("count of each item is like the following :"+ str(dictCount))


#  Exercise 5: Given a two list of equal size create a Python set such that it shows the element from both lists in the pair
# Expected Output:
#
# First List  [2, 3, 4, 5, 6, 7, 8]
# Second List  [4, 9, 16, 25, 36, 49, 64]
# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}


FirstList = [2, 3, 4, 5, 6, 7, 8]
SecondList = [4, 9, 16, 25, 36, 49, 64]


result = zip(FirstList,SecondList)

resultset= set (result)
print(resultset)

#
# First Set  {65, 42, 78, 83, 23, 57, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}
#
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

firstset ={-6,52,63,98,1,4,7}
secondset={2,7,98,44,59,39,-6,52}

print(firstset)
print(secondset)

intersection = firstset.intersection(secondset)
print(intersection)

for i in intersection :
    firstset.remove(i)

print(firstset)

##############################################################3


firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
# Expected Output:
#
# First Set  {57, 83, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}
#
# First set is subset of second set - True
# Second set is subset of First set -  False
#
# First set is Super set of second set -  False
# Second set is Super set of First set -  True
#
# First Set  set()
# Second Set  {67, 73, 43, 48, 83, 57, 29}


firstSet = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

print("First set is subset of second set -", firstSet.issubset(secondSet))
print("Second set is subset of First set - ", secondSet.issubset(firstSet))

print("First set is Super set of second set - ", firstSet.issuperset(secondSet))
print("Second set is Super set of First set - ", secondSet.issuperset(firstSet))

if (firstSet.issubset(secondSet)):
    firstSet.clear()

if (secondSet.issubset(firstSet)):
    secondSet.clear()

print("First Set ", firstSet)
print("Second Set ", secondSet)



rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print(rollNumber)
print(sampleDict)


rollNumber[:] =[ i for i in rollNumber if i in sampleDict.values()]

print(rollNumber)

##############################################################################################

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

print("Dictionary's values - ", speed.values())

toList =[]
for value in speed.values() :
    if (value not in toList):
        toList.append(value )

print(toList)


#Exercise 10: Remove duplicate from a list and create a tuple and find the minimum and maximum number


sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
print(sampleList)
uniqu =  list(set(sampleList))
print(uniqu)

tu= tuple(uniqu)

print(tu)



#############################################
#fil input output


count = 0
with open("sample.text", "r") as fp:
    lines = fp.readlines()
    count = len(lines)
with open("newFile.txt", "w") as fp:
    for line in lines:
        if (count == 3):
            count -= 1
            continue
        else:
            fp.write(line)
        count-=1

# str1, str2, str3 = input("Enter three string").split()
# print(str1, str2, str3)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i +" AHMAD  "+ j for i, j in zip(list1, list2)]
print(list3)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resList = [x+y for x in list1 for y in list2]
print(resList)



my_list = ["Hello", "Python"]
print("-".join(my_list))
aList = [5, 10, 15, 25]
print(aList[::-2])
aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)


sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])


aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])


sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)


resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)


sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)


list1 = ['xyz',  'zara','PYnative']
print (max(list1))



aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)


sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)


x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)

for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break











############################################
i=""
for p in range(10):
    for j in range (10):
        for k in range (10):
            for l in range (10):
                i+="*"
                print(i)




###########################################################################################

#OOP


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())



#####################################################
class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)



#########################################

import random

#gues game


def get_guess():
    return  list(input("whats your guess"))

def generate_code():
    digits=[str(num)for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues (code,user_guess):
    if user_guess==code:
        return "code cracked"
    clues=[]
    for ind ,num in enumerate(user_guess):
        if num==code[ind-1]:
            clues.append("match")
        elif num in code :
            clues.append("Close")
    if clues==[]:
         return ["Nope"]
    else:
         return clues


print("welcoeme fgfdgvsfdg")
secrete_code = generate_code()
clue_report =[]
while clue_report != "code cracked":
    guess=get_guess()

    clue_report =generate_clues(guess,secrete_code)
    print("here your guess")
    for clue in clue_report :
        print(clue)






