import contactos as c
if (__name__ == '__main__'):
    isAddData = True
    contactos = {}
    menu = '1. Agregar\n2. Editar\n3. Eliminar\n4. Buscar\n5. Salir'
    contactos = c.VerifyFile()
    while(isAddData):
        c.f.os.system('cls')
        print(menu)
        try:
            op =int(input(':'))
        except ValueError:
            print('Error en la opción ingresada')
            c.f.os.system('pause')
            continue
        else: 
            if (op == 1):
                c.f.os.system('cls')
                c.AddContact(contactos)
            elif (op==2):
                c.ModifyData(contactos)
            elif (op==3):
                c.DelData()
            elif (op==4):
                data = c.SearchData()
                print(data)
                c.f.os.system('pause')
            elif (op==5):
                rta ='x'
                while (rta not in ['N','n','']):
                    rta = input('Desea salir No(n/N) Enter(Si) Salir?')
                    isAddData = bool(rta)
