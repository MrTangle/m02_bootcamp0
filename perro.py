class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p

    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")

    def __str__(self):
        return "Soy el perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)

salchicho = Perro("Salchicho", 3, 12)
lola = Perro("Lola", 8, 1.5)
miko = Perro("Miko", 8, 3)
salchicho.ladrar()
lola.ladrar()

#make me a class which send an email to an address defined in an argument

def victor(self, **kwargs):
    diccionario = {}
    for k, v in kwargs.items():
        diccionario.update({k: v})
    print(diccionario)
    
victor(caca=3, ibhad=2, ojdnh=65, ano=23, adhdo=44)

'''
    def ladrar(self, *args, **kwargs): # que hace la ele, ponme ejemplo
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
'''