agenda = {}
count = 0
class Contacto:
    def __init__(self, nombre, telefono, email, dni):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.dni = dni
    def añadir_contacto(self):
        contacto = [self.nombre, self.telefono, self.email, self.dni]
        global count
        count += 1
        agenda[count] = contacto

    def mostrar_contacto(self):
        print(agenda)

    def buscar_contacto(self):
        busqueda = []
        b = list(agenda.values())
        for a in b:
            if self.dni in a:
                busqueda.append('True')
            else:
                busqueda.append('False')
        if 'True' in busqueda:
            print("Ya está agendado")
        else:
            print("NO está agendado")


x = Contacto("Luis", 945336094, "lnunez@gmail.com", 46451254)
x.añadir_contacto()
x.mostrar_contacto()

y = Contacto("Alberto", 981602457, "lroldan@gmail.com", 29306695)
y.añadir_contacto()
y.mostrar_contacto()

z = Contacto("Alberto", 981602457, "lroldan@gmail.com", 29306695)
z.buscar_contacto()


