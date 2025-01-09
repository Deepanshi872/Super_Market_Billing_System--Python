#print ("Hello world") 

#name = "Deepanshi"
#age = 24 
#Job = "umenployeed"
#print("my name is :", name) 
#print("my age is:", age) 

#a= 2
#b= 3
#Diff = a-b
#print(Diff)  

# Arithmetic Operators
'''a= 7
b= 9
multi = a*b

print(multi) 
print (a % b) # remainder
print (a**b) #a^b
'''

# Relational Operators
'''a= 2
b= 3

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b) '''

# Assignment Operators
''' num = 9
num+= 10
num-=2
print(num)'''

# Logical Operators
'''a= 8
b=8

print(not (a>b)) 
print("and operator: ", (a==b) and (a<b))
print ("or operator:", (a==b) or (a>b))
'''

'''name = input("Enter your name:")

print("welcome", name )'''

'''num1= int(input("first number:"))
num2= int(input("second number:"))
print("sum:" ,num1+num2)'''

'''side = int(input("enter square side:"))
side2= int(input("enter square side:"))
print("Square area:", side*side2)'''

'''num1= int(input("enter your number:"))
num2= int(input("enter youe 2 number:"))

print (num1>=num2)'''

'''name = input("enter your name")
print ("Welcome:", name)'''

#Typecasting: 
# 1. Implicit casting: Automatically converts a smaller type to a larger type size. 
# 2. Explicit casting: Manually converts a larger type to a smaller size type.

'''example of explict
a= "23"
b= 2
c= int(a) + b
print (c)'''

#Operators: Operators are used to perform operations on variables and values.
# 1. Arithmetic Operators (+, -, *, %, ^, //(floor division), /)
# 2. Relational Operators (a==b, a!=b, a>=b, a<=b)
# 3. Assignment Operators (+=, -=,*=)
# 4. Logical Operators (and , or, not)
#5. Membership Operators (In , not in)
#6. Identity Operators (is, is not)

#conditional Statement
# 1. If statement
'''price = 250
seats= int(input("enter seats:"))
Total= price * seats

combo= input("Do you want a combo (yes/no):")
if combo== "yes":
    Total +=300 

print(Total)'''

#2. If else Statement
'''markes= int(input("enter your marks:"))

if markes > 70:
    print("Pass")
else:
    print("Fail") '''

#3. If elif else Statement:

'''marks= int(input("enter your marks:"))

if marks >=90:
    print ("A Grade")
elif marks >=80 and marks<90:
    print ("B Grade")
elif marks >=70 and marks<80:
    print("C Grade")
else: 
    print("D Grade") '''

#4. nested if statement ( next step occurs if the current step is cporeect E.g if we login our social media with an email which does not
#exist then it won't take me to the password only if my email is correct it will take me to the password)
'''
username = "Deepanshi"
password= "Manju.321"

un= input("enter your username:")
if un== username:
    ps =input("enter your password:")
    if ps==password:
        print("login sucessful") 
    else:
        print ("enter valid password")
else: 
    print("enter valid username") '''

#loops: it help us repeat something in the exact same way

#1. For Loop (is used when we know exact number of how many times we need to exceute the programme or also used to iterate)
'''a= input("enterr your answer")

for i in a:  #for is the keyword for for loop
    print (i)''' 


'''for i in range(1,70,2):    #range(Start value,start value+1, step)
    print(i)'''

'''num= int(input("enter your number"))

for i in range(1,11):
    print(num, "x", i ,"=", i*num)'''

'''sum= 0

for i in range(0,190):
    if i%2!=0:
        sum+=i
        print(sum)'''

#2. While Loop - when you don't know till when to run loop but know the certain condition which needs to be fulfilled
'''a= 1

while a <10:
    print(a)
    a+=1'''

'''repeat= "Yes"
while repeat== "Yes":
    num1= int(input("Enter your number:"))
    num2= int(input("Enter your number:"))
    print(num1+num2)
    repeat= input("Do you want to add more numbers: ")'''

#3. While True- infinite loop. While true says i'm always true. to stop the loop we use a break statement
'''while True: 
    num1= int(input("enter your number:"))
    num2= int(input("enter your second number:"))
    print(num1+num2)
    repeat= input("do you want to add more numbers?")
    if repeat=="no":
        break'''

'''for i in range(1,21):
    if i >=13:
        break
    else:
        print(i, "no song is playing")'''

'''for i in range(1,32):
    if i<=12:
        continue
    else:
        print(i, "no. of song playing")'''

#4. Nested loop:  A nested loop means a loop statement inside another loop statement. That is why nested loops are also called “loop inside loops“.

'''for i in range(1,4): #counting rows
    for j in range(1,11): #counting columns
        print(i*j, end=" ")
    print()'''

#Theater booking system:
'''price= 280
while True:
    amount= 0

    name= input("enter your name:")
    phone_number=input("enter your phone number:")
    seat=int(input("enter seat you want:"))

    Total_amount= price*seat

    print("""Press 1 to add a combo of Rs. 150. 
    Press 2 to add the combo of Rs. 250.
    Press 3 to add the combo of Rs. 350
    Press 4 to make a luxury meal box of Rs.500""")

    Combo_Choice= input("Do you want a combo:")
    while True:
        if Combo_Choice=="yes":
            Choice= int(input("Enter the combo number you want to choose:"))
            Quantity= int(input("Enter quantity:"))
            if Choice==1:
                Total_amount+=150*Quantity
                
            elif Choice==2:
                Total_amount+=250*Quantity
                
            elif Choice==3:
                Total_amount+=350*Quantity
                
            elif Choice==4:
                Total_amount+=500*Quantity

            repeat= input("Do you want to add more combo?")
            if repeat=="no":
                break
            
            print("Your total amount is:",Total_amount)

        Next_person= input("next person:")
        if Next_person=="Yes":
            break'''

#Strings

'''a="Deepanshi"
print(type(a))'''

#indexing: position of our string in a memeory(+ve,-Ve)

"""a="Deepanshi"
print(a[2])"""

#slicing: if we want data based on position\

'''a= "Deepanshi is a good girl"

print(a[0:9]) '''

#functions in string

#1. length
"""a= "Deepanshi"
print(len(a))
print(a.count(""))"""

#lists: Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data.

#Features of list:
#1. It can store multiple data also of multiple datatype
#2. Each value is comma seprated
#3. List should be in square brackets
#4. Lists are mutable (onece created it can be changed) and ordered

'''a= [1, "mango", "Deepanshi", 29, "Friday", "Birthday", 2.5]

print(a[:3])
a.append("manju")
a.insert(2,"Gaurav")
print(a)'''

#list comprehension and Iterations

#add even number to the list

'''a= [1,2,3,34,5,66,78,9,9,0,98,345,46]

even=[]

for i in a:
    if i%2==0:
        even.append(i)

print(even)'''

#Replace in list

'''a= [1,32,43,64,56,5,57]

a[1], a[4]= a[4], a[1]

print(a)'''

#write a program to count the number of words with length of atleast 5 and has frst and last letter similar

'''a= ["Sunita", "Deepanshi", "Manju", "Ishita", "Ishi", "K.K", "Rajpal", "Mum", "Madam"]

count= (0)
for i in a:
    if len(i)>= 5 and i[0]==i[-1]:
        count+= 1

print(i)'''

#Sets: A Set in Python programming is an unordered collection data type that is iterable and has no duplicate elements.
#{} are mandatory, values are comma seprated, sets give distinct values 

'''a= {1,3,4,56,67,134,143,146}
b= {123,1,2,3,4,542,67,65,143}

print(a.union (b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a-b)

print(a.symmetric_difference(b))
print(a^b)'''

#Covert the list into sets and and find common data 
'''a= [1,2,3,44, 134, 143,45,56,64]
b= [13,432,52,1,3,34,45,44,45,54]

print(set(a) & set(b))'''

#Dictionaries: Dictionaries are used to store data values in key:value pairs. 
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
#Dictionaries are comma seprated
#They are kept iunside{} 
#key cannot be duplicate

'''d= {"name": "Deepanshi", "Gender": "Female", "City": "Delhi", "Grade": "MBA"}

print(d["City"])
print(d["name"])
print(d["Grade"])

d["marks"]= 90

print(d)

print(d.keys())
print(d.values())
print(d.items())

for i,j in d.items():
    print(i,"-",j)'''

# [] it is a lsit, () it is a tuple, {} it is a Dictionaries, set() it is a emplty set

'''db= {}

print( """ 
Press 1 to insert values
Press 2 to update values
Press 3 to remove values
Press 4 to view values""")

while True:
    choice= int(input("Enter number of your choice: ")) 

    if choice==1:
        country= input("Enter your country: ").capitalize()
        capital= input("Enter capital of the country: ").capitalize()
        db[country] = capital

    elif choice==2:
        country= input("Enter updated country: ").capitalize()
        capital= input("Enter updated capital: ").capitalize()
        db[country]= capital

    elif choice==3:
        country= input("Delete this vaue from database: ").capitalize()
        del db[country]

    elif choice==4: 
        for i,j in db.items():
            print(i, "-", j)

    else: print("invalide input...please try again")'''

#Nested Dictionaries: a nested dictionary is a dictionary inside a dictionary. It's a collection of dictionaries into one single dictionary.

'''comapany= {"EI001": {"Name":"Deepanhsi","Gender": "Female", "Salary": 30000, "Designation": "Intern"},
"EI002": {"Name": "Namju", "Gender": "Female", "Salary": 70000, "Designation": "CHO"},
"EI003": {"Name": "Gaurav", "Gender": "Male", "Salary": 100000, "Designation": "Software Engineer"}}

print(comapany["EI002"] ["Salary"])'''

#How to create your own functions in python

#def= when youy define a function
'''def hello():
    print("hello world")

hello()

def add():
    print(12+23)

add()'''

#return 

'''def hello():
    return"hello world"
print(hello())
'''

'''def add():
    print(12+23)
    print(34-23)
    print(34/45)

add() '''

#parameters and arguments: information that are passed into a function

'''def add(a,b): 
    return a + b 

print(add(2,3))
print(add(3,4))'''

'''def company(name,salary):
    print("name is", name)
    print("salary is", salary)

n= input("Enter  your name:")
s= int(input("Enter your salary:"))

company(n,s)'''

#recursive function: functions that calls itself.

#Fibonacci Numbers using Native Approach
'''n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()'''

'''import pandas as pd

# Create an empty DataFrame with specific columns
empty_df = pd.DataFrame(columns=['Name', 'Age', 'Country'])

print(empty_df)'''

#concate 2 tuple:

'''num1= (1,"a", "True")
num2=(2,3,4)

print(num1+num2)'''

'''import numpy as np

n1= np.zeros((5,5))
print(n1)'''

'''import pandas as pd
data= [1,"true", 2.3]

series=pd.Series(data)

print(series)
print(type(series))'''

'''import pandas as pd

df = pd.DataFrame({'vehicle': ["Kia", "KTM", "Nano", "Splender"], 'Type': ["Car", "Bike", "Car", "Bike"]})
print(df)

df.groupby('Type').count()'''

#how to create datframes from list

'''import pandas as pd

df= pd.DataFrame()

cars= ["Nano", "KIA", "Swift", "BMW"]
bikes= ["KTM", "Splender", "Bullet", "Honda"]

df["cars"]= cars
df["bikes"]=bikes

print(df)'''

#create dataframes from dictorines

'''import pandas as pd

df= pd.DataFrame()

cars= ["Nano", "KIA", "Swift", "BMW"]
bikes= ["KTM", "Splender", "Bullet", "Honda"]

d= {"care":cars, "bikes":bikes}
df= pd.DataFrame(d)

print(df)'''

'''menu={}

print("""
Insert 1 to install the value
Insert 2 to update the value
Insert 3 to delete the value""")

while True:
    choice= int(input("enter your choice:"))

    if choice==1:
        name= input("enter dish name:").capitalize()
        price= float(input("enter dish price:"))
        menu[name]= price
        print(menu)

    elif choice==2:
        name= input("enter dish name you want to update:").capitalize
        price= float(input("enter updated price of the dish:"))
        menu[name]= price
        print(menu)

    else:
        name= input("enter dish name you want to delete:").capitalize()
        del menu[name]
        print("this dish is deleted from menu")'''

'''db= {}

print( """ 
Press 1 to insert values
Press 2 to update values
Press 3 to remove values
Press 4 to view values""")

while True:
    choice= int(input("Enter number of your choice: ")) 

    if choice==1:
        country= input("Enter your country: ").capitalize()
        capital= input("Enter capital of the country: ").capitalize()
        db[country] = capital

    elif choice==2:
        country= input("Enter updated country: ").capitalize()
        capital= input("Enter updated capital: ").capitalize()
        db[country]= capital

    elif choice==3:
        country= input("Delete this vaue from database: ").capitalize()
        del db[country]

    elif choice==4: 
        for i,j in db.items():
            print(i, "-", j)

    else: print("invalide input...please try again")'''

#functions: 1. inbuid functions e.g print, input, type 2. user defined e.g def()

'''def hello():
    print("hello i'm deepanshi.")

for i in range(5):
    hello()'''

'''def num():
    print(2+3)
    print(3*4)
    print(2-4)
num()'''

#return: The Python return statement marks the end 
# of a function and specifies the value or values to pass back from the function. 

'''def hello():
    return "hello world"

print (hello())'''

#Parameters and arguments in functions:

'''def add(a, b): #parameters
    return a+b

print(add(2, 4)) #arguments
print(add(43, 3))'''

'''def comapny(name, salary):
    print("name is: ", name)
    print("salary is: ", salary)

name1= input("enter name: ")
salary2= int(input("enter salary: "))
comapny(name1, salary2)'''

#recursive function: when a function call itself again and again

'''def factorial(x):
    if x ==1:
        return x
    else:
        return x * factorial(x-1)
    
print(factorial(6))'''

#lambda function: use to create fake/tempory function 

'''x=lambda a:a #anonomous
print(x(2))'''

'''x= lambda a,b,c: a+b*c
print(x(2,3,4))'''

#in-built modules= files in python which we can create and import to utilize it 
#1. user defined modules
#2. in-built modules

'''import datetime

print(datetime.datetime.now())'''

#Numpy: NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
'''import numpy as np

print(np.array([1,2,3]))'''
'''for _ in range(12):
    print("This will be printed 12 times.")'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("C:/Users/deepa/Downloads/imdb_movies.csv")

# Convert the 'date_x' column to datetime format
df["date_x"] = pd.to_datetime(df["date_x"])

# Print the 'date_x' column
print(df["date_x"])

# Calculate and print the sum of null values in each column
null_counts = df.isnull().sum()
print(null_counts)

# Filling the null values
df["genre"] = df["genre"].fillna("Unavailable")
df["Crew"] = df["Crew"].fillna("Unavailable")
print(df["Crew"])

# Create and display a histogram
sns.histplot(x="score", data=df)
plt.show()
