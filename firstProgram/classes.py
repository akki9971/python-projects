# single use class
class person:
    fist_name="something"
    last_name="something"
    age="something"


# multiuse class
class persons:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return self.first_name + ' ' + self.last_name

sumer = persons("sumer", "rana",23)
akib = persons("akib","ali",24)

print(sumer.full_name())
# print(akib.name, akib.age)