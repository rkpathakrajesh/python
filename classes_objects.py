# working with CLASSESS and OBJECTS

# CLASSES HAVE PROPERTIES AND BEHAVIOURS
"""
E.G. PHONE HASE PROPERTIES BRND, COLOUR, PRICE, DIMENSIONS ETC.
                BEHAVIOUR HOW IT WORKS, WHAT ARE THE FEATURE OF THE PHONE LIKE CAN TAKE PICTURES,
                CAN MAKE PHONE CALL, CAN ACCESS INTERNET ETC.

CLASS IS BLUEPRINT 
AND OBJECTS ARE REAL THINGS COVERED IN SIDE OF THAT CALSS 
"""
# CLASS NAME ALWAYS STARTS WITH CAPITAL LETTER

class Person:
    def __init__(self, name, age):
        # below are properties
        self.name = name
        self.age = age
        # below are behaviours
    def walk(self):
        print(self.name + 'is walking...')
    def speak(self):
        print( 'Hello my name is ' + self.name + ' and I am ' + str(self.age)+ ' ' +'years old')

John = Person('JOHN', 25)
Mariam = Person('Mariam', 20)

print(John.name + '  ' + str(John.age))
John.walk()
John.speak()
print('-------------------')
print('+++++++++++++++++++')
print('-------------------')
print(Mariam.name + '  ' +  str(Mariam.age))
Mariam.walk()
Mariam.speak()
