# While loop examples
n = 1
while n < 11:
    print(n)
    n += 1

#Get years to reach balance
balance = 1000
rate = 1.02
years = 0
while balance < 5000:
    balance *= rate
    years += 1
print("It takes " + str(years) + " years to reach $5000.")

#for loop examples

for i in [1,2,3,4,5]:
    print(i)
    
for name in ["Jane", "John", "Matt", "George"]:
    print(name)

for i in range(0,10):
    print(i)