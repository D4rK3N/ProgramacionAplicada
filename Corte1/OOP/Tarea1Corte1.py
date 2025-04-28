class perro:

    def __init__(self, nombre, raza):

        self.nombre = nombre 
        self.raza = raza

    #metodos

    def ladrar(self):
        print (f"guau")
    
    def descripcion(self):
        print (f"WOF! holi, me llamo {self.nombre} y soy un {self.raza}.")

#instancias clase perro

mi_perro = perro("max","doberman")
segundo_perro = perro("rocky","chiester savanni")
tercer_perro = perro("matias","puro criollo")

#acceder a los metodos y atributos

print(mi_perro.nombre)
mi_perro.ladrar()
perro.descripcion(segundo_perro)
perro.descripcion(tercer_perro)



