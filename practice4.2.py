import pyfiglet
result =pyfiglet.figlet_format('samin noroozi')
print(result)

hour=int(input("Enter hour: "))
minute=int(input("Enter minutes: "))
second=int(input("Enter secodes: "))
sec=hour*3600+minute*60+second
print("second: ",sec)