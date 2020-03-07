class A:
    def __init__(self):
        self.message = "This is from Class A\n"
    
    def __str__(self):
        return self.message


class B(A):
    def __init__(self):
        super().__init__()
        self.age = 18

    def __str__(self):
        return super().__str__() + "Age: " + str(self.age)

b  = B()
print(b)