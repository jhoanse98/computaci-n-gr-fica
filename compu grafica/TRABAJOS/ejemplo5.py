def cuadrado(a):
  return a**2

def correccion(a,b=5):
    return a+b

#print cuadrado(5)
#print correccion(8)

def operaciones(a,b):
    suma=a+b
    resta=a-b
    return suma, resta

s,r=operaciones(4,7)
print s,r
