'''
OOP
----

FEATURES OF OOP
1. Enscapsulation
2. Inheritance
3. Polymorphism
    a. Method overloading
    b. Method overriding
4. Abstraction(Interface)

''''''
Online News Portal
    User
        name, mobile, email, username, password
        register(), update(), view(), login(), delete()
    News
        topic, date, details, authors, category
        add(),view(), update(), delete()
    comment
        fullname, email, comments, 
        add(), view(), delete()

Online Student Enrollment
    Course
        title duration fee shift affiliation department status
        add(), view() update() delte()

    Enrollments
        student course  



Online Job Portal
    User
        user, mobile, email, username, password
        register(), update(), view(), login(), delete
    Job
        title detail requirement salary company vacancy_no category
        register(), update(), view(), login(), delete()
    Jobseeker
    Application
        user job

Online shopping (E-commerce)
    User
        name, mobile, username, password, image, cv,type, status
        register(), update(), view(), login(), delete()
    Customer 
    Seller    
    Product
        name price details stock featuresn category brand types
        add(),view(), update(), delete()
    Order
        user product date

'''
'''
class User:
    full_name= ''
    mobile= ''
    email = ''
    address = ''
    password = ''
    type = ''

    def register(self):
        pass
    
    def view(self):
        pass
    
    def login(self):
        pass

    def search(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass 


us
'''


class Animal:
    # __color='' #private
    # __height='' #protected
    # __weight=''

    # def __init__(self):
    #     self.color = ''
    #     self.height = ''
    #     self.weight = ''


    def __init__(self, color, height, weight):
        self.__color = color
        self.__height =height
        self.__weight = weight

    #setters & getters
    def setColor(self, value):
        self.__color = value
   
    def getColor(self, value):
        return self.__color

    def move(self):

        print('It moves')




# animal = Animal()
# animal.move()
# animal.weight = "4ft"


class Dog(Animal):
    def __init__(self, color, height, weight, food):
        self.food = food
        super().__init__(color, height, weight)

class Crocodile(Animal):
    pass

class Bird(Animal):
    pass


dog = Dog('white', '2ft', '10kg','abc')
print(dog)



s