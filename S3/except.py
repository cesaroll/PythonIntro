#How to handle exceptions

try:
    num = 3/0
    print(num)
except:
    print('Cannot divide by zero')
    
print('Finished')

try:
    num = int(input('Enter a number: '))
    print(num)
    
    aFile = open('mud.py')
    print(aFile.readline())
    
except ValueError:
    print('Not a number')
    
except IOError:
    print('Cannot Open File')