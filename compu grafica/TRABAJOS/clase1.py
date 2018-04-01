#ejemplo1
class estudiante:
    def __init__(self, nombre='juan'):
        self.nombre=nombre
        self.apellido='perez'
        self.edad=35

    def Nombre(self):
        return self.nombre + ' ' + self.apellido


e=estudiante('ana')
#print e.Nombre

print e.Nombre()
e1=estudiante()
e1.nombre='luisa'
e1.apellido='gomez'
print e1.Nombre()
