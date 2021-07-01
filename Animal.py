class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return f"animal: {self.name}, {self.age}"


class Dog(Animal):
    def speak(self):
        print("Ham Ham")

    def __str__(self):
        return f"dog: {self.name}, {self.age}"


class Person(Animal):
    id = 1

    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = set()
        self.tag = Person.id
        Person.id += 1

    def get_friends(self):
        return self.friends

    def add_friend(self, new_friend):
        if new_friend:
            self.friends.add(new_friend)

    def __str__(self):
        return f"Person {self.tag}: {self.name}, {self.age}"




cat = Animal(4)
print("Cat's age is:", cat.get_age())
print("Cat's name is:", cat.get_name())
cat.set_name("Tom")
print(cat)
cat.size = 'Big'
print(cat.size)

print("------")
lassie = Dog(10)
lassie.set_name('Lassie')
print(lassie)
lassie.speak()

print("------")
ion = Person("Ion", 22)
maria = Person("Maria", 21)

print(ion)
print(maria)
print(maria.get_friends())
maria.add_friend("Ion")
maria.add_friend("George")
maria.add_friend("George")
print(maria.get_friends())
print(maria)
print(Person.id)

