class Animal:
    def __init__(self):
        self.som = "Este animal faz um som genérico"

    def falar(self):
        print(self.som)

class Cachorro:
    def __init__(self):
        self.som = "O cachorro está latindo."

    def falar(self):
        print(self.som)

class Gato:
    def __init__(self):
        self.som = "O gato está miando."

    def falar(self):
        print(self.som)



gato1 = Gato()
gato1.falar()
print("*" * 30)
animal1 = Animal()
animal1.falar()
print("*" * 30)
cachorro1 = Cachorro()
cachorro1.falar()
