import numpy
import math

b = 0

v1_linspace = numpy.linspace(0, 100, 1000)
v2_linspace = numpy.linspace(0, 100, 10000)
v3_linspace = numpy.linspace(0, 100, 100000)
v4_linspace = numpy.linspace(0, 100, 1000000)

v1_arange = numpy.arange(0, 100, 0.1)
v2_arange = numpy.arange(0, 100, 0.01)
v3_arange = numpy.arange(0, 100, 0.001)
v4_arange = numpy.arange(0, 100, 0.0001)



def f_q1(x, b):
    return pow(x,3) + pow(x,2) + b

def d2_x(v, b, f):
    lista = [0]
    h = v[1] - v[0]
    for x in v[1:-1]:
        lista.append((f(x+h, b) - 2*f(x,b) + f(x-h, b))/pow(h,2))
    lista.append(0)
    return numpy.array(lista, dtype=object)

def d1_frente_x(v, b, f):
    lista = []
    h = v[1] - v[0]
    for x in v[:-1]:
        lista.append((f(x + h, b) - f(x, b))/h)
    lista.append(0)
    print(lista)
    return numpy.array(lista)

def d1_tras_x(v, b, f):
    lista = [0]
    h = v[1] - v[0]
    for x in v[1:]:
        lista.append((f(x, b) - f(x - h, b))/h)
    return numpy.array(lista)

def d1_central_x(v, b, f):
    lista = [0]
    h = v[1] - v[0]
    for x in v[1:-1]:
        lista.append((f(x + h, b) - f(x - h, b))/(2*h))
    lista.append(0)
    return numpy.array(lista)

def d1(x):
    return 3*pow(x,2) + 2 * x

def d2(x):
    return 6*x + 2

def dif_normalzera(v, b, f):
    lista = []
    for x in v:
        lista.append(f(x))
    return numpy.array(lista)

print(d2_x(v3_arange, b, f_q1)[0:10])
print(dif_normalzera(v3_arange, b,  d2)[0:10])
