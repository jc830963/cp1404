from person import *
# define one object
p = Person('joanne', 20)
print('My name is', {p.name}) and print('My name is', {p.age})
print(p)
# define second object
p2 = Person('Tony', 30)
print('My name is', p2.name)
print('My name is', p2.age)
print(p2)
# define a list of 3 person object
list_of_3_people = [Person('Sarah'), Person('Phuc', 20), Person('Tiri', 21)]
for person in list_of_3_people:
    print(person)
print(p.my_num)
print(p2.my_num)
print(person.my_num)
