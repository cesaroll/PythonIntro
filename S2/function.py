def square(num):
    return num * num

def convertTemp(temp, scale):
    if scale == "C":
        return (temp - 32.0) * (5.0/9.0)
    elif scale == "F":
        return temp * 9.0/5.0 + 32

    
number = 12
print(square(number))


temp = input("Enter a temperature: ")
scale = input("Enter the scale to convert to: ")

converted = convertTemp(temp, scale)

print("The converted temp is: " + str(converted))


def onePerLine(str):
    for i in str:
        print(i)

word = input("Enter a phrase: ")
onePerLine(word)