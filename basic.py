'''name and  variables

name = "Abiral Blon"
age=24
salary= 50000.00
is_married= True

print("Name: "+name)
print("Salary: ", name)
print(f'Age {age}\tSalary:{salary}')
print('Marital status: ', is_married)


name = input("ENTER YOUR NAME: ")
age= input("ENTER YOUR AGE")
salary= input("ENTER YOUR SALARY")

print(name, salary)

print("mMr/Mrs",name,"Your salary is :",float(salary)*0.85)
'''
'''
 Operators
'''
'''
    1. Arithmetic:  + - * / ** // 
    2. Logical:  and or not
    3. Relational: <  > >= <= == 
    4. Assignment: = += -= *= **= /= //= %=
    5. Concatenation: + ,
    6. Membership: in        not in
    7. Identical: is     is not

'''

# a=100
# b=10
# c=15
# print(a>b and a==c)
# print(a != b)


'''
Conditional statements
1. if 
2. if...else
3. if...elif...else
'''

# a=input("Enter the value of a ")
# b=input("Enter the value of b ")
# if a>b:
#     print("A is greater than B ")
# elif b>a:
#     print("B is greather than A")
# else:
#     print("A and B are equal")6


# num = int(input("Enter the number "))

# if num%2==0:
#     print("NUMBER IS EVEN")
# else:
#     print("NUMBER IS  ODD")


# Loops in Python
# 1. for
# 2. while

'''

for(initializatio; condition; increment/decrement){body}
for (a=1;a=10;a++)
for i in range(10,2,-2):
    print(i)
'''


# Print if a given number is prime or composite'''
'''
num =int(input("Enter the number:"))
for i in range(2,num//2+1):
    if num%i==0:
        print("NUmber is composite")
        break
else:
    print("Number is prime")
'''


# Print if a given number is prime or composite using while loop
'''
i=2
while(num//2+1):
    if num%i==0:
        print("Composite")
        break
    i+=1
else:
    print("Prime")

'''

# print factorial of a user givern number.
'''
fact = 1
for i in range(1,num+1):
    fact *=i
print("Factorial = ",fact)

'''

# print factors of a user given number
'''
print("The factors are : ")
for i in range(1,num+1):
    if num%i==0:
        print(i)

'''

#fibonacci series  0 1 1 2 3 5 8 13 .....
'''
a=0
b=1

print(a)
print(b)

for i in range(100):
    c=a+b
    if(c<100):  #for series less than 100
        print(c)
        a=b
        b=c
    else:
        break

while a+b<100:
    c=a+b
    print(c)
    a=b
    b=c
'''


# Mulitiplication of number
'''
n=5
for i in range(1,11):
    print(n,'*',i,"=",n*i)
    print(f'{n}*{i}={n*i}')
        
print("Welcome "*10)

n1=10
n2=10
for i in range(1,n1+1):
    for j in range(1,n2+1):
        print(i,"*",j,"=",i*j, end="      ")
    print()
'''

'''
*               1               1           55555           54321
**              22              12          4444            4321
***             333             123         333             321
****            4444            1234        22              21    
*****           55555           12345       1               1   
'''

for i in range(5):
    for j in range(i+1):
        print('*', end=" ")
    print()


for i in range(5):
    for j in range(i+1):
        print(i+1, end=" ")
    print()

for i in range(5):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

print()

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()