class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):
        return self.base * self.altura


base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))


rectangulo1 = Rectangulo(base,altura)

print(f" el resultado es: {rectangulo1.area_rectangulo()}")