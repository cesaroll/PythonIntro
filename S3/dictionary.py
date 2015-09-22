import os

os.system('cls')

#Create Dictionary
beatles = {'John':'Guitar', 'Paul':'Bass','George':'Guitar','Ringo':'Drums'}
#Notice dictionary do not print in order
print(beatles)

#Value of index "John"
print(beatles['John'])

#how many items are there in the dictinary
print(len(beatles))

#Get keys only
print(list(beatles.keys()))

#Get Values only
print(list(beatles.values()))

#Display each name with associated instrument
for name in beatles.keys():
    print(name + ' plays ' + beatles[name])

#Other way to get value from dictionary
print(beatles.get('Paul'))

#Change values of a given key
beatles['Paul'] = ['Bass',  'Guitar', 'Keyboards']
print(beatles['Paul'])

#Add new item to dictionary
beatles['Pete'] = 'Drums'
print(beatles)

#remove item
print(beatles.pop('Pete'))
print(beatles)