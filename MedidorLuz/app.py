import csv

csv_file = open("/PROYECTOS/MedidorLuz/medidor_de_luz.csv", "w+")

csv_writer = csv.writer(csv_file)



costo_KW = 0.69
aseo = 20
lectura_anterior = 4979.67
print(f"La lectura del mes anterior fue de: {lectura_anterior} KWs")
LecturaActual = float(input("Ingrese la lectura actual: "))
if LecturaActual <= lectura_anterior:
    print("La lectura actual de tu medidor no puede ser menor o igual que la lectura del mes anterior. Vuelve a intentarlo.")

else:        
    consumoKW = LecturaActual - lectura_anterior
    print(f"Tu consumo de este mes es de: {consumoKW:.2f} KWs")

    aPagar = consumoKW * costo_KW + aseo
    print(f"Y tu monto a pagar es de: {aPagar:.2f} soles.")


csv_writer.writerow(["Costo Kw", " ", "Aseo", " ", "Lectura Anterior", " ", "Lectura Actual"])
csv_writer.writerow([costo_KW, " ", aseo, " ", lectura_anterior, " ", LecturaActual])

csv_file.close()

