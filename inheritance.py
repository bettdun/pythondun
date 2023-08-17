# inheritance allows one class to inherit attibutes
# and methods from another class
class animals:
    def __int__(self,name):
        self,name=name
    def speak(self):
        pass
class dog(animals):
    def speak(self):
        return "woof"
class cat(animals):
    def speak(self):
        return "woow"
# this are objects
Doggy=dog("buddy")
cat=cat("whisker")
print(dog.speak())
print(cat.speak())
