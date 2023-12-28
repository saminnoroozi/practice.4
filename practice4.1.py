import pyfiglet
result =pyfiglet.figlet_format('samin noroozi')
print(result)

second=int(input("Enter your seconds: "))
hour=(second//3600)
minute=(second%3600)//60
sec=second%60
print(hour,":",minute,":",sec)

