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

for i in student_info_collection:
    print(student_info_collection[i]['name'])