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

    def appearance(self):  
        print("My  dog is {}".format(self.color))
 

# Object instantiation
pesh = Dog("Pesh", "green", "barks")
Tee = Dog("Tee", "blue", "barks")
 
# Accessing class attributes
print("Pesh is a {}".format(pesh.attr1))
print("Tee is also a {}".format(Tee.attr1))
 
# Accessing instance attributes
print("My name is {}".format(pesh.name))
print("My name is {}".format(Tee.name))

# Accessing class methods
pesh.speak()
Tee.speak()

pesh.appearance()
Tee.appearance()
 