class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def speak(self):  
        print("This dog {}".format(self.sound))
 

# Object instantiation
pesh = Dog("Pesh", "green", "barks")
Tee = Dog("Tee", "blue", "barks")
 
# Accessing class attributes
print("Pesh is a {}".format(pesh.attr1))
print("Tee is also a {}".format(Tee.attr1))
 
# Accessing instance attributes
print("My name is {}".format(pesh.name))
print("My name is {}".format(Tee.name))


# Accessing instance attributes
print("My color is {}".format(pesh.color))
print("My color is {}".format(Tee.color))


# Accessing class methods
pesh.speak()
Tee.speak()
 
# Accessing instance attributes
print("My name is {}".format(pesh.name))
print("My name is {}".format(Tee.name))