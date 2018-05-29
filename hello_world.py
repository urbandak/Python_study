# this is one example
message = 'I told frind "hello world"'
print(message)

message = "hello crash python course world"
print(message.upper())

print(message.title())

print(message.lower())

first_name = "wang    "
last_name = "cheng    "
full_name = first_name.rstrip() + "_" + last_name.rstrip()

print('my \nname is ' + full_name.title()+'.\n')

full_name = first_name + "_" + last_name

print('my \nname is ' + full_name.title()+'.\n')

result = 2 + 3 * 2 + 0.1
print(result)

result = 0.2 + 0.1
print(result)

result = 3 * 0.1
print(result)

age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)

print(3.0/2.0)

import this

bicycles = ['tek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[2])

print(bicycles[1].title())

message = 'my first bycyle is ' + bicycles[0] + "."
print(message.title())
print(message)

bicycles[1] = "test-new-cycle"

print(bicycles)

bicycles.append("last cycle")

print(bicycles)

motocycles = []
motocycles.append("test1")
motocycles.append("test 2")
motocycles.append("test 3")
print(motocycles)

motocycles.insert(1, "test-001")
print(motocycles)
del motocycles[1]
print(motocycles)

motocycles.append("test5")
print("1:" + str(motocycles))

#poped_motocycles = motocycles.pop()
#print("2" + str(motocycles))
#print("3 " + str(poped_motocycles))

# motocycles.pop(0)
# print(motocycles)

print(motocycles)
# if want to use this value, which will be removed. need store it to one var, and then use this var
var = "test1"
motocycles.remove(var)
print(motocycles)
print("removed cycles is " + var)

# usage for "Sort"
cars = ["bmw", "toyato", "subaru"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))

cars.reverse()
print(cars)

print(len(cars))

# this is very good usage,compared with C
print(cars[-1])

for car in cars:
    print(car.title() + "\t")
    print("I can't want to see you next trick " + car.title())
print("this is end!!!")

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(0,11):
    square = value **2
    squares.append(square)
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))

print(max(digits))

print(sum(digits))




squares = [value**2 for value in range(1,11)]
print(squares)


