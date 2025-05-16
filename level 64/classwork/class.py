class human:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def _str_(self):
        return f"my name is {self.name} and I am {self.age}"
    
    def my_name (self):
        return self.name

    def my_name_age(self):
        return self.name
    