import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print(RPS(2))
print(RPS.ROCK)
print(RPS["ROCK"])
print(RPS.ROCK.value)

sen = 'Pranesh'

print(sen.endswith('h'))

# # Complex
comp= 3+5j
print(comp.imag)


#sys.exit()

# #LIST
list=['fire','ash',True]
list.append('water')
list.extend(['nothing']) 
list.insert(0,'air')
list.remove('air')
list.pop()
del list[0]
list.clear()
# list.sort(key=str.lower()) #Prevent from capital and small order

num =[2,4,1,4,5]
num.reverse()

num.sort(reverse=True)

(sorted(num,reverse=True)) #1st sort and reverse it
num.copy()


# #Dict
car={
    "Model":"Benz",
    "Year":2025
    }

print(car.get('Year'))
print(car.keys())
print(car.values())
print(car.items())
print("Model" in car)
print(car.update({"price":20000}))
print(car.popitem()) #return as tuple



def add(*args):
    sum=0
    for n in args:
        sum = sum + n
    print(sum)
add(2,6)

def multiple(**arg):
    print(arg)
multiple(first = "Pranesh",second = "Ragu")    



# #Recursion 
def addone(num):
    if num >= 9:
        return num+1
    total = num+1
    print(total)

    return addone(total)
newtotal = addone(0)
print(newtotal)


# #Closure is a function having access to the scope of its parent function after the parent function has returned

def Parent(person):
    coins = 3
    def play():
        nonlocal coins
        coins -=1
        if coins >1:
            print(person + " has " + str(coins) + " Coins left")
        elif coins == 1:
            print( person + " has " + str(coins) + " Coins left")
        else:
            print(person + " has no Coins left")    
    
    return play

tommy = Parent("tommy")

tommy()
tommy()
tommy()


def multiply(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = multiply(3)

times5 = multiply(5)

print(times5(times3(2)))



# # %s Formating
person = "Pranesh"
coins = 3

message = "\n%s has %s coins left" % (person,coins)
print(message)

# string.format() method

message = "\n{1} has {0} coins left".format(person,coins)
print(message)



# num = 3
# print(f"{2.25 * num:.2f}")  # Using f-string formatting
# print(f"{2.25 * num:.2%}")


# #Lambda
def builder(x):
    return lambda num: num + x

add_10 = builder(10)
print(add_10(7))


num = [1,2,3,4,5,6]

print(sum(num))

sqre = map(lambda num:num * num,num)

# print(list(sqre))



from functools import reduce
names = ['Pranesh','Vengatesh','Siva']

char = reduce(lambda acc,curr: acc + len(curr),names,0)

print(char)



# #Classes

class vechicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = vechicle('Tesla', 'Model Y')

my_car.moves()
print(my_car.make)
print(my_car.model)
my_car.get_make_model()


# #Inheritance

class Airplane(vechicle):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print('Flies along...')

class Truck(vechicle):
    def moves(self):
        print('Rumbles along...')

class Golfcart(vechicle):
    pass #hidden new class


cessna = Airplane('Cessna', 'Skyhawk','N-12345')
mack = Truck('Mack','Pinnacle')
golfwagon = Golfcart('Yamaha', 'GC100' )



cessna.get_make_model()


# #   Polymorphism
for v in (my_car,cessna,mack,golfwagon):
    v.get_make_model()
    v.moves()



# #   Try and except
try:
    x = input('Enter a name:')
    print(x)

except NameError:# or value error
    print('Name error')

except ZeroDivisionError:
    print('Please dont divided by error' )

except Exception as error:
    print(error)

else:
    print('No error')

finally:
    print('Whatever Im gonna print')


#Classes
class Person:
    def __init__(self,name,age):#pass for empty class 
        self.name = 'Pranesh'
        self.age = 21

p1=Person('Pranesh',21)
print(p1.name)
    

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Nothing(Animal):
    pass #pass without assigning anything


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls Parent's constructor
        self.breed = breed

    def info(self):
        print(f"{self.name} is a {self.breed}")

dog = Dog("Buddy", "Labrador")
dog.speak()  # Inherited from Animal
dog.info()   # Defined in Dog
