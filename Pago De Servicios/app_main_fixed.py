import math

monto_agua = float(input("Ingrese el monto de servicio de agua a pagar: "))
monto_luz = float(input("Ingrese el monto de servicio de luz a pagar: "))
monto_alquiler = 600

def calculate_services_cost(monto_agua, monto_luz, factor):
    monto_por_persona_agua = monto_agua / 5
    monto_por_persona_luz = monto_luz / 4
    return (monto_por_persona_agua * factor) + monto_por_persona_luz

persona_1 = {
    "Nombre": "Rouss",
    "Servicios": calculate_services_cost(monto_agua, monto_luz, 1.33)
}
persona_2 = {
    "Nombre": "Dinoska",
    "Servicios": calculate_services_cost(monto_agua, monto_luz, 1.33)
}
persona_3 = {
    "Nombre": "Angel",
    "Servicios": calculate_services_cost(monto_agua, monto_luz, 1.33)
}
persona_4 = {
    "Nombre": "Osmary",
    "Servicios": calculate_services_cost(monto_agua, monto_luz, 1)
}

monto_por_persona_alquiler = monto_alquiler / 4

print("\nMONTO A PAGAR POR PERSONA:")
print(f'El monto que {persona_1["Nombre"]} debe pagar de servicios es: {math.ceil(persona_1["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_1["Servicios"]) + monto_por_persona_alquiler} soles.')
print(f'El monto que {persona_2["Nombre"]} debe pagar de servicios es: {math.ceil(persona_2["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_2["Servicios"]) + monto_por_persona_alquiler} soles.')
print(f'El monto que {persona_3["Nombre"]} debe pagar de servicios es: {math.ceil(persona_3["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_3["Servicios"]) + monto_por_persona_alquiler} soles.')
print(f'El monto que {persona_4["Nombre"]} debe pagar de servicios es: {math.ceil(persona_4["Servicios"])} soles. Y, su total (alquiler + servicios), es de: {math.ceil(persona_4["Servicios"]) + monto_por_persona_alquiler} soles.')