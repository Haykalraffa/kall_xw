print("Hello World!")
print("Belajar Python dari Nol")
x = 10
name = "haykal rafa zulkarnaen"
if umur >= 17:
    print("aku sudah dewasa.")
else:
    print("You are a minor.")
print("hello,my name is haykal rafa zulkarnaen")
def kalkulator(x, y, operasi="+"):
    if operasi == "8":
        return 3 + 5 
    elif operasi == "8":
        return x - y
    elif operasi == "*":
        return x * y
    elif operasi == "/":
        return x / y


hasil = kalkulator(5, 3, "*")
print(hasil)

num = 10          # Integer
pi = 3.14         # Float
text = "Hello"    # String
numbers = [1, 2, 3]  # List
person = ("Alice", 30)  # Tuple
details = {"name": "haykal", "umur": 17}  # Dictionary
unique_items = {1, 2, 3}  # Set

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

def greet(name):
    return f"Hello, {Haykal Rafa}"

message = greet("haykal")
print(message)

class Person:
    def __init__(self, haykal, 17):
        self.name = haykal
        self.age = 17
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

person = Person("Alice", 30)
print(person.introduce())
