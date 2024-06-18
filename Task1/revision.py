"""
str = "nitesh"
len1 = len(str)
print(len1)

str1 = "kumar"
len2 = len(str1)
print(len2)

str3 = str + " "+ str1
print(str3)

print(str[2])
print(str1[3])

print(str3[1:4])

print(str3[2:7])

print(str3[4:len(str3)])

print(str3[3:])

print(str3[:5])

print(str3[-3])

print(str3[-8])

print(str3[-7:-1])



str4 =  "my Name is Nitesh!"

print(str4.endswith("sh!"))

print(str4.capitalize())

print(str4.replace("Nitesh","Kumar"))

print(str4.find("Nitesh"))

print(str4.count("is"))

print(str4.count("i"))



# 1
str = input("Enter your first name : ")
print(len(str))
print(str.count("$"))


marks = int(input("Enter your marks: "))
if(marks>= 90):
    print("Grade A")
elif(marks>= 80):
    print("Grade B")
elif(marks>= 70):
    print("Grade C")
else:
    print("Grade D")



a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is greatest")
else:
    print("c is greatest")



num = int(input("Enter a number : "))
if (num % 7 == 0):
    print("it is multiple of 7")
else:
    print(" it is not multiple of 7")



m1 = "Fighter"
m2 = "3idiots"
m3 = "animal"

l1 = []
l1.append(m1)
l1.append(m2)
l1.append(m3)
print(l1)



l1 = ["m","a","d","a","m"]
l2 = l1.copy()
print(l2)
l2.reverse()

if(l1 == l2):
    print("Palindrome")
else:
    print("Not Palindrome")

t1 = ("C","D","A","A","B","B","A",)
print(t1.count("A"))
print(t1)
print(t1[1:])
print(t1[-6:-1])


l4 = ["C","D","A","A","B","B","A"]
l4.sort()
print(l4)

dict = {"name":"nitesh", 
        "rollno":"21cs36", 
        "branch":"CS"}
print(dict)

dict1 = {
    "mark1":78,
    "mark2":67,
    "maark3":34
}
print(dict1)



dict3 = {
    "name" : "nitesh",
    "age" : 21,
    "marks": [91,90,80,95,34],
    "grade" : ("A","B","C","A","D"),
    "rollno" : 2136,
    12 : 45,
    23.67 : "fjnfknv"
}
print(dict3)

dict3["branch"] = "CS"

print(dict3)

print(dict3["age"])
print(dict3["grade"])


# nested dictionary
dict = {"marks": {
    "maths":89,
    "chem":78,
    "phy":90,
    "eng":98},
    "age":21,
    "name":"nitesh"}
print(dict)
print(dict["marks"]["maths"])
print(dict["marks"]["chem"])

print(dict.keys())
print(dict.values())
print(dict.items())

print(list(dict.keys()))
print(list(dict.values()))
pairs = list(dict.items())
print(pairs)
print(pairs[0])
print(pairs[1])
print(pairs[2])

print(dict["name"])
print(dict.get("name"))

#print(dict["name2"])    # it gives error 
print(dict.get("name2"))  # it doesn't give error
print("hi")

dict.update({"city": "Far"})
print(dict)

dict1 = {"village":"Tilpat"}
dict.update(dict1)
print(dict)

dict.update({"name":"kumar"})
print(dict)

dict1.update({"village":"Til"})
dict.update(dict1)
print(dict)

dict.pop("village")
print(dict)



set1 = {1,2,2,"heello","hii","India","hii"}
print(set1)
print(len(set1))

set2 = set()
print(type(set1))

set1.add(78)
print(set1)

set1.remove("India")
print(set1)

print(set1.pop())
print(set1)

set1.clear()
print(set1)
print(len(set1))

set1.add((4,5,7))
print(set1)

#set1.add([2,4,6])
#print(set1)

print(len(set1))

set2 = {1,2,3,5,7,9}
set3 = {2,4,5,6,8,10}

print(set2.union(set3))

print(set2.intersection(set3))



dict = {"table":["a piece of furniture","list of facts and figures"],"cat":"a small animal"}
print(dict)


set = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print("total Classroom are:",len(set))

sub1 = input("Enter marks of sub1 :")
sub2 = input("Enter marks of sub2 :")
sub3 = input("Enter marks of sub3 :")

dict = {}
dict.update({"sub1":sub1})
print(dict)
dict.update({"sub2":sub2})
print(dict)
dict.update({"sub3":sub3})
print(dict)



set = {9,9.0,8,8.0}           # in hashing of 8 and 8.0 is same
print(set)

set1 = {9,"9.0","8",8.0}
print(set1)

set2 = {("int",9),("float",9.0)}
print(set2)




x = 1
while x <= 5:
    print("Nitesh")
    x = x + 1


y = 1
while (y <= 10):
    print("Hello")
    y = y + 1



i = 1
print("Loop Started")
while i <= 10:
    print("i :", i)
    i = i + 1
print("Loop Ended")


i = 15
print("Loop Started")
while (i >= 1):
    print("i :", i)
    i = i - 1
print("Loop Ended")



i = 1
while (i <= 100):
    print("i :", i)
    i = i + 1

i = 100
while ( i >= 1):
    print("i :", i)
    i = i - 1


i = int(input(" Enter the table no :"))
j = 1
while (j <= 10):
    print(i,"*",j,"=", i*j)
    j = j +1 


j = 1
print("Square of no from 1 to 10")
while j <= 10:
    print(j,"^",j,"=",j*j)
    j = j +1


x = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(x):
    print(x[index])
    index = index + 1


x = (1,4,9,16,25,36,49,64,81,100)
y = int(input("Enter a no to search : "))
i = 0
while i<len(x):
    if(x[i]==y):
        print("found at index", i)
    i = i + 1




x = [1,4,9,16,25,36,49,64,81,100]
for i in x:
    print(i)


x = [1,4,9,16,25,36,49,64,81,100]
y = int(input("Enter a no to search : "))
index = 0 
for i in x:
    if(i == y):
        print("yes found at index : ", index)
    index = index + 1



for i in range(5):
    print("hello")

for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(0,10,2):
    print(i)


for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

n = int(input("enter no: "))
for i in range(11):
    pass
    print(n,"*",i,"=",n*i)



n = int(input("enter no :"))
i = 0
j = 0
while i<=n:
    j = j + i
    i = i + 1
print(j)

n = 5
j = 0
for i in range(1,n+1):
    j = j+i
print("addition of ",n "is :",j)


n = 5
j = 1
for i in range(n,1,-1):
    j = j*i
print("Factorial of",n,"is :",j)



n= 5
i = 1
j = 1
while i<=n:
    j = j*i 
    i = i + 1
print("Factoral of",n,"is :",j)

n = 5
j = 1
for i in range(1,n+1):
    j = j*i
print("Factorial of",n,"is :",j)


def average(a,b,c):
    return (a+b+c)/2

avg  = average(1,2,3)
print(avg)

def average1(x,y,z):
    avg = (x+y+z)/2
    print(avg)

average1(1,2,3)

def average1(x,y,z):
    avg = (x+y+z)/2
    print(avg)
    return avg

average1(1,2,3)
avg1 = average1(2,3,4)
print(avg1)


def lin(a):
    return len(a)

c = lin([2,3,4,5,6,7,6,2,9,0])
print(c)

def lan(a):
    print(a)

lan([2,3,4,5,6,7,6,2,9,0])


def Factoral(n):
    i = 1
    j = 1
    for i in range(1,n+1):
        j = j*i
    print(j)
Factoral(5)

def factorial(n):
    i = 1
    j = 1
    while i <= n:
        j = j * i 
        i = i + 1
    return j

fac = factorial(5)
print(fac)


c = [2,3,4,5,6,7,6,2,9,0]

def lin(a):
    print(len(c))

lin(c)

def lan(a):
    print(a, end= " ")

lan(c)
print()


def convert(usd):
    return usd*83

ui = convert(2)
print("INR :", ui)


def number(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")
    
number(int(input("enter a no:")))

"""

def recursion(n):
    if n==0:
        return
    print(n)
    recursion(n-1)

recursion(5)
