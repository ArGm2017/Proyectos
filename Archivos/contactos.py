import funciones as f
def VerifyFile():
    if(f.checkFile('agenda.json')):
        return f.ReadFile('agenda.json')
    else:
        f.CreateFile('agenda.json')

def AddContact(data : dict):
    id  = str(len(data)+1).zfill(3)
    nombre = input('Ingrese el nombre del contacto: ')
    email = input(f'Ingrese el email de {nombre}: ')
    celular =  input(f'Ingrese el Nro Cel de  {nombre}: ')
    tel = input(f'Ingrese el Nro Telefonico de  {nombre}: ')
    dataContact ={
        'id': id,
        'nombre': nombre,
        'email': email,
        'celular': celular,
        'tel': tel
    }
    data.update({id: dataContact})
    f.AddData('agenda.json', {id: dataContact})


def SearchData():
    data = f.ReadFile('agenda.json')
    criterio = input('Ingrese el nombre del contacto a buscar: ')
    for key,value in data.items():
        if(criterio.upper() in value['nombre'].upper()):
            return key,value
    f.os.system('pause')

def DelData():
    data = f.ReadFile('agenda.json')
    criterio = input('Ingrese el nombre del contacto a eliminar: ')
    for key,value in data.items():
        if(criterio.upper() in value['nombre'].upper()):
            data.pop(key)
            f.UpdateFile('agenda.json',data)
            print("Se eliminó correctamente el contacto")
            break
    f.os.system('pause')

def ModifyData(data):
    myContact = SearchData()
    keys,valores = SearchData()
    print(myContact)
    print(valores)
    f.os.system('pause')