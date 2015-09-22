import os

os.system('cls')

beatles = ['John', 'Paul', 'George', 'Ringo']

print(beatles)

print(len(beatles))
print(beatles[0])
print(beatles[1:])
print(beatles[0:2])
print(beatles[2:4])

#print in sorted order
print(sorted(beatles))

#permanently sort list
beatles.sort()
print(beatles)

#permanently reverse list
beatles.reverse()
print(beatles)

#add to the list
beatles.append('Pete')
print(beatles)

#remove from list, the last one
beatles.pop()
print(beatles)

#find index item in list
beatles.append('Pete')
print(beatles)
idx = beatles.index('Pete')
print(idx)

#Delete by index
del beatles[idx]
print(beatles)
