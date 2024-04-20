#Aplicacion para calcular el monto a pagar por persona
import math

monto_agua = float(input("Ingrese el monto de servicio de agua a pagar: "))
monto_luz = float(input("Ingrese el monto de servicio de luz a pagar: ")) 
monto_por_persona_luz = float(monto_luz / 4)
monto_por_persona_agua = monto_agua / 5
monto_alquiler = 600
monto_por_persona_alquiler =  monto_alquiler / 4

persona_1 = {
    "Nombre":"Rouss", 
    "Servicios": (monto_por_persona_agua * 1.33) + monto_por_persona_luz * 1}
persona_2 = {
    "Nombre":"Dinoska", 
    "Servicios": (monto_por_persona_agua * 1.33) + monto_por_persona_luz * 1}
persona_3 = {
    "Nombre":"Angel", 
    "Servicios": (monto_por_persona_agua * 1.33) + monto_por_persona_luz * 1}
persona_4 = {
    "Nombre":"Osmary", 
    "Servicios": (monto_por_persona_agua * 1) + monto_por_persona_luz * 1}
persona_5 = "Emma y Mau"

print("\nMONTO A PAGAR POR PERSONA:")
print(f'El monto que {persona_1["Nombre"]} debe pagar de servicios es: {math.ceil(persona_1["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_1["Servicios"]) + monto_por_persona_alquiler} soles.')
print(f'El monto que {persona_2["Nombre"]} debe pagar de servicios es: {math.ceil(persona_2["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_2["Servicios"]) + monto_por_persona_alquiler} soles.')
print(f'El monto que {persona_3["Nombre"]} debe pagar de servicios es: {math.ceil(persona_3["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_3["Servicios"]) + monto_por_persona_alquiler} soles.')
print(f'El monto que {persona_4["Nombre"]} debe pagar de servicios es: {math.ceil(persona_4["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_4["Servicios"]) + monto_por_persona_alquiler} soles.')

#Comentario 2