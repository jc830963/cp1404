num_of_people = 0
total_age = 0
age = int(input('Enter age (-1 to quit): '))
while age >= 0:
    num_of_people += 1
    total_age += age
    age = int(input('Enter age (-1 to quit): '))

if num_of_people > 0:
    print('Average age of {} is {:.2f}'.format(num_of_people, total_age / num_of_people))
else:
    print('No valid age is entered.')

try:
    number = int(input("? "))
    print(10 / number)
except ValueError:
    print("Not a valid integer")
except ZeroDivisionError:
    print("can't divide by zero")
except:
    print("some other exception happened")
    print("Finished")
