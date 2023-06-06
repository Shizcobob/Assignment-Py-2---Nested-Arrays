x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1 
# def changeToFifteen():
#     x[1][0] = 15
#     return x
# print(changeToFifteen())

# #2
# def changLastName():
#     students[0]['last_name'] = 'Bryant'
#     return students
# print(changLastName())

# #3
# def changename():
#     sports_directory['soccer'][0] = 'Andres'
#     return sports_directory
# print(changename())

#  #4
# def changeNum():
#     z[0]['y']=30
#     return z
# print(changeNum())


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]        



#6     
def iterateDictionary2(key_name, some_list):
    for name in students:
        print(name[key_name])
print(iterateDictionary2('first_name', students))



# #7     
# def iterateDictionary2(students):
#     for name in students:
#         print(name['last_name'])
# print(iterateDictionary2(students))


# 5
# def iterateDictionary(students):
#     for name in students:
#         print(name)
# print(iterateDictionary(students))



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# 8
def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]) ,key)
        for val in some_dict[key]:
            print(val)
    

    
print(printInfo(dojo))







