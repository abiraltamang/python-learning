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
    Application
        user job

Online shopping (E-commerce)
    User
        name, mobile, username, password, image, cv,type, status
        register(), update(), view(), login(), delete()
    Product
        name price details stock featuresn category brand types
        add(),view(), update(), delete()

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
    
    @staticmethod
    def view():
        pass
    
    def login():
        pass

    def search():
        pass

    def update():
        pass

    def delete():
        pass 

