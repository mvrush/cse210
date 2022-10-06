""" These are notes about classes gleaned from W3Schools """

# To create a class , use the keyword 'class'. Here's an example:
class MyClass:
    x = 5 # 'x' is now a Property of the 'MyClass' class.

# This is how we create an Object using the class named 'MyClass'
# We will create an object named 'p1', and print the value of x.
# Following 2 lines calls the 'MyClass' object and assigns the entire thing to the variable 'p1' which then makes 'p1' an object of 'MyClass'
# At that point we can call properties from the 'MyClass' class.
p1 = MyClass()
print(p1.x) # Output will be '5'


# The __init__() function. It uses 2 underscores before and after 'init'
# The __init__() function is built-in. All classes have the function.
# The __init__() function is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties or ATTRIBUTES,
# or other operations that are necessary to do when the object is being created.

# Here we create a class named 'Person', use the __init__() function to assign properties or ATTRIBUTES and their values for name and age:
# Note: the 'self' parameter is a reference to the current instance of the class, and is used to access variables that belong in the class.
class Person:
    def __init__(self, name, age): # We use 'def' to define a function. We assigned 3 parameters 'self', 'name' and 'age'
        self.name = name # This is a property or ATTRIBUTE of the 'Person' class using parameters from the __init__() function.
        self.age = age # This is a property or ATTRIBUTE of the 'Person' class using parameters from the __init__() function.
# Note: The __init__() function is called automatically every time the class ie being used to create a new object.

    # A handy thing to do is create a __str__() function to see a string representation of the object.
    # Whenever the object is called it will have access to the __str__() and it will represent whatever you put in it.
    # Heres an example of a __str__() function in the 'Person' class
    def __str__(self):
        return f"{self.name}({self.age})" # Will return whatever parameters are assigned to 'name' and 'age' as a string you can print

    # We can also create Object Methods.
    # Methods in Objects are functions that belong to the object.
    # Here is a Method (or function) held in the Person class. We will name it 'myfunc()' and give it the 'self' parameter
    # Using the 'self' paramter means it will hold the 'self.name' and 'self.age' properties.
    def myFunc(self):
        print(f"Hello, I'm {self.name}, and I am {self.age} years old, and I like to party!")

# Here we call the 'Person' class and give it a 'name' and 'age' parameter and assign that to
# an object named 'p1'. It will contain the __init__() function and accept the passed parameters to that function.
p1 = Person("Spankman", 69)

# We can then call each property from the new 'p1' Object which follows the properties specified in the 'Person' class
print(p1.name) # Prints the 'name' property in the 'p1' Object which was created from the 'Person' class
print(p1.age) # Prints the 'age' property in the 'p1' Object which was created from the 'Person' class

# We can also use the __str__() function to print out the defined string in that function.
# It's also part of the 'p1' object which holds the 'Person' class with parameters.
print(p1)

# We also have access to the 'myFunc()' method defined in the 'Person' class. We will use it here.
# We already defined the 'p1' Object above which holds the 'Person' class and gave it parameters. Now we call the function.
p1.myFunc()

# You can modify Object Properties or ATTRIBUTES like this:
p1.age = 21
# Now the 'age' property is '21'. We can use 'myFunc()' to show the change
p1.myFunc()


""" REMOVE THIS COMMENT TO SEE THE 'del' KEYWORD IN ACTION

# You can also straight up delete properties or ATTRIBUTES on Objects using the 'del' keyworkd
del p1.age
# Now what happens when we use the 'myFunc()' function?
p1.myFunc()
# YOU GET AN ERROR CUZ YOU DELETED IT!!

# You can also delete the entire Objects using the 'del' keyword
del p1
# Now what error do we get when we try to call the 'myFunc()' function from that Object?
p1.myFunc()

"""

