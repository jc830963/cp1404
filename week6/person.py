class Person(object):
    # define class variable
    # class variables are shared among objects
    my_num = 20

    def __init__(self, name='unknown' , age=18 ):
        # define instance
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'
