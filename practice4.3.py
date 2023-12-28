import pyfiglet
result =pyfiglet.figlet_format('samin noroozi')
print(result)

n=int(input("Enter your number: "))
x=[0,1]
for i in range(1,n):
    number= x[i]+x[i-1]
    x.append(number)

print(x)

