
# Working with Loops

cars = ['BMW','Maruti', 'Marcedes','Tesla','honda']
for car in cars:
    if car=='honda':
        print(car.upper())
    else:
        print(car.capitalize())


# Working with while Loop

number = 0
while number <= 10:
    print(number)
    number = number + 1
else:
    print('While loop is ended and value of number is ' + str(number))

