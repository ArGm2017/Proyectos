import turtle
import random
from time import sleep


# Dimensiones de la pantalla
ancho_pantalla = 600
alto_pantalla = 400

# Tamaño del segmento de la serpiente
segmento_tamanio = 20

# Velocidad inicial del juego
velocidad = 0.1

# Lista que guarda los segmentos de la serpiente
segmentos = []

# Posición inicial de la cabeza de la serpiente
x_cabeza = 0
y_cabeza = 0

# Dirección inicial de la serpiente
direccion = "derecha"

# Manzana
x_manzana = random.randint(-ancho_pantalla//2 + segmento_tamanio, ancho_pantalla//2 - segmento_tamanio)
y_manzana = random.randint(-alto_pantalla//2 + segmento_tamanio, alto_pantalla//2 - segmento_tamanio)

# Puntuación
puntuacion = 0

# Juego en marcha
jugando = True


def dibujar_segmento(x, y):
  """
  Dibuja un segmento de la serpiente en la pantalla.
  """
  turtle.penup()
  turtle.setposition(x, y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(segmento_tamanio / 2)
  turtle.end_fill()

def mover_cabeza():
  """
  Mueve la cabeza de la serpiente en la dirección actual.
  """
  global x_cabeza, y_cabeza, direccion

  if direccion == "arriba":
    y_cabeza += segmento_tamanio
  elif direccion == "abajo":
    y_cabeza -= segmento_tamanio
  elif direccion == "derecha":
    x_cabeza += segmento_tamanio
  elif direccion == "izquierda":
    x_cabeza -= segmento_tamanio

def dibujar_manzana():
  """
  Dibuja una manzana en la pantalla.
  """
  turtle.penup()
  turtle.setposition(x_manzana, y_manzana)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(segmento_tamanio / 2)
  turtle.end_fill()

def comer_manzana():
  """
  Comprueba si la serpiente ha comido la manzana.
  """
  global x_cabeza, y_cabeza, x_manzana, y_manzana, puntuacion, velocidad

  if x_cabeza == x_manzana and y_cabeza == y_manzana:
    x_manzana = random.randint(-ancho_pantalla//2 + segmento_tamanio, ancho_pantalla//2 - segmento_tamanio)
    y_manzana = random.randint(-alto_pantalla//2 + segmento_tamanio, alto_pantalla//2 - segmento_tamanio)
    puntuacion += 1
    velocidad *= 0.95

    # Añadir un nuevo segmento a la serpiente
    segmentos.append((x_cabeza, y_cabeza))

def mover_segmentos():
  """
  Mueve todos los segmentos de la serpiente.
  """
  global segmentos

  for i in range(len(segmentos)-1, -1, -1):
    if i == 0:
      segmentos[i] = (x_cabeza, y_cabeza)
    else:
      segmentos[i] = segmentos[i-1]

def chocar_con_borde():
  """
  Comprueba si la serpiente ha chocado con el borde de la pantalla.
  """
  global jugando

  if x_cabeza > ancho_pantalla//2 - segmento_tamanio or x_cabeza < -ancho_pantalla//2 + segmento_tamanio or \
     y_cabeza > alto_pantalla//2 - segmento_tamanio or y_cabeza < -alto_pantalla//2 + segmento_tamanio:
    jugando = False

def chocar_con_si_misma():
  """
  Comprueba si la serpiente ha chocado consigo misma.
  """
  global jugando, segmentos

  for i in range(len(segmentos)-1, 0, -1):
    if x_cabeza == segmentos[i][0] and y_cabeza == segmentos[i][1]:
      jugando = False

def actualizar_pantalla():
  """
  Actualiza la pantalla con la nueva posición de la serpiente y la manzana.
  """
