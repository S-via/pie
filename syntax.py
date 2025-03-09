# List Example
fruits = ["apple", "banana", "cherry"]
print("List Example:", fruits)

# Tuple Example
coordinates = (3, 7)
print("Tuple Example:", coordinates)

# Dictionary Example
person = {"name": "Alice", "age": 25, "is_student": True}
print("Dictionary Example:", person)

# Arithmetic Operators
num1 = 10
num2 = 3
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
mod_result = num1 % num2
exp_result = num1**num2
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Exponentiation:", exp_result)

# Comparison Operators
age = 25
is_adult = age >= 18
is_teenager = age >= 13 and age < 18
print("Is adult?", is_adult)
print("Is teenager?", is_teenager)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


def check_age(age):
    if age < 18:
        print("You are a minor.")
    elif 18 <= age < 21:
        print("You are an adult, but not yet allowed to drink.")
    else:
        print("You are a legal adult.")


# Call the function with a specific age
check_age(20)

# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {"key": "value"}
bool = True

# Get and print the type of each variable
print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool))


# define a class
class Dog:
    sound = "bark"  # class attribute


# Create an object from the class
dog1 = Dog()

# Access the class attribute
print(dog1.sound)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.make} {self.model} {self.year}"




my_car = Car("Honda", "Civic", 2020)
print(my_car.get_info())


num1 = "5"
num2 = 3
result = num1 * num2
print(result)
