import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

def greet():
   if now.hour < 12:
       print("Good morning!")
   elif now.hour < 18:
       print("Good afternoon!")
   elif now.hour < 22:
        print("Good evening!")
   else:
        print("Good night!")
greet()



