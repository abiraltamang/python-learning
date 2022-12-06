'''
Colections in Python
1. Tuple : immutable, indexed, ordered
2. List : mutable, indexded, ordered
3. Set : immutable but new elements can be added, unindexed, unordered
4. Dictionary

(Range)

student_info = ['Ram', 'Bsc. CSIT', 5, 'Kathmandu']

student_list= ['ram', 'shyam', 'hari', 'sita', 'gita']
student_tuple=('ram', 'shyam', 'hari', 'sita', 'gita')
student_set={'ram', 'shyam', 'hari', 'sita', 'gita'}
student_dict={
    12001:"ram",
    12002:"Shyam",
    12003:"hari",
    12004:"geeta",
    12005:"nirvik",
}
user_info_dict = {
    'name':'Abiral Blon',
    'age':23,
    'salary':453434,
    'is_married':True
}

print(student_list)
print(student_tuple)
print(student_set)

print(user_info_dict['name'])

for i in user_info_dict:
    print(i,':',user_info_dict[i])

for i in student_list:
    print(i)
'''


# Multidimensional collection
'''
a=[[],[],[],[]]
b=[(),(),(),()]
c=((),(),(),())
d=([],[],[],[])
e={'key1':{},'key2':{},'key3':{},'key4':{}}
f={'key1':[],'key2':[],'key3':[],'key4':[]}
f={'key1':(),'key2':(),'key3':(),'key4':()}
'''
'''
student_info_collection ={
    '12001':{
        'name':'Abiral BLon',
        'address':"Koteshwor",
        'phone':9808633373,
    },
    '12002':{
        'name':"Nirvik Karki",
        'address':'Pepsicola',
        'phone':984541254
    },
    '12003':{
        'name':"Bhupesh Upadhyaya",
        'address':'Koteshwor',
        'phone':985421452
    }
}
'''

# for i in student_info_collection:
#     print(student_info_collection[i]['name'])


#days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
'''n=int(input('Enter a number:'))
if n<8 and n>0:
    print(days[n-1])
else:
    print("Invalid number")
    '''


#Functions in python
'''
1. Parameterized and nonparameterized functions
2. 
'''


# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# def add(a,b):
#     return a+b

# sum =add(num1,num2)
# print(sum)

'''
def add_np():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print (num1+num2)
add_np()
    
'''


# def prime_number_checker():
#     num= input("Enter the number to check if it is prime : ")
#     if num.isdigit():
#         a=int(num)
#         for i in range(2,a//2+1):
#                 if a%i==0:
#                     print("NUmber is composite")
#                     break
#         else:
#             print("Number is prime")
#     else:
#         print("Invalid entry")



# def prime_number_checker():
#     try:
#         num= input("Enter the number to check if it is prime : ")
#         a=int(num)
#         for i in range(2,a//2+1):
#                 if a%i==0:
#                     print("NUmber is composite")
#                     break
#         else:
#             print("Number is prime")           
#     except Exception as e:
#         print("Invalid entry", e)


questions = [
    'What is  area of Nepal?',
    'What is height of mount everest?',
    'What is the first prime minister of Nepal?',
    'Ehat is the population  of nepal?',
    "First nepali movie is :"
]
options = [
    ('147181 sqkm', '161456 sqkm','141281 sqkm','246765 sqkm'),
    ('8848', '4474', '8490', '9984'),
    ('Bhimsen Thapa', 'Ram Baran Yadav', 'Jalnath Khanal', 'KP oli'),
    ('lots of', 'lots  of lots ', 'low', 'moderate'),
    ('Aama', "Bagh", "Sungur Muskurayo", 'Haan Bdr Jilke')
]

answers = ['a','a','a', 'd','a']
# answers = ['147181 sqkm','8848','Bhimsen Thapa', 'moderate','Aama']

score = 0

def show(n):
    print(questions[4])
    print('a. ', options[n][0])
    print('b. ', options[n][1])
    print('c. ', options[n][2])
    print('d. ', options[n][3])
    choice = input("Enter a/b/c/d : ")
    global score
    # if choice !='a' or choice !='b' or choice != 'c' or choice!='d':
    if choice not in ['a', 'b', 'c','d']:
        print('Invalid selection')
        choice = input("Enter a/b/c/d : ")

    if(choice == answers[n]):
        score += 1

for i in range(len(questions)):
    show(i)

print("Your score is : ",score)