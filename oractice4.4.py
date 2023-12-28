import pyfiglet
result =pyfiglet.figlet_format('samin noroozi')
print(result)

x=int(input("Enter yor nymber: "))
n=1
i=1
while i <=x:
    i+=1
    n*=i
if n==x:
    print("yes")
else:
    print("no!!")