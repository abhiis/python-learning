class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):  #that's it. Dog has inherited all the methods of mammal
    def bark(self):
        print("bark")


class Cat(Dog):
    def purr(self):
        print("purr")


dog1 = Dog()
dog1.bark()
dog1.walk()

cat1 = Cat()
cat1.purr()
cat1.bark()
cat1.walk()