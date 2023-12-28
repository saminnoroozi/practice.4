import pyfiglet
result =pyfiglet.figlet_format('samin noroozi')
print(result)

number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
kmm=1
if number1<number2:
    min=number1
else:
    min=number2

for i in range(1,min+1):
    if (number1%i==0) and (number2%i==0):
        kmm=i

print("your kmm is: ",kmm)